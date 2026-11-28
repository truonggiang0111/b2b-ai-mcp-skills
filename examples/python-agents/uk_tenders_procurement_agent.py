"""LangChain Tool example for UK Gov Contracts Finder OCDS & Direct Buyer Emails.

Demonstrates:
1. Zero-key queries to official UK Contracts Finder REST v2 + OCDS endpoints
   extracting buyer organization, ``.gov.uk`` / NHS / council emails, GBP budgets,
   deadlines, and notice URLs.
2. Wrapping the Python tools for LangChain (``langchain_core.tools.StructuredTool``
   + ``ChatOpenAI.bind_tools``) with a clean stdlib fallback when optional LangChain
   dependencies are not installed.
3. Optional scaled Apify enrichment via ``ttyan0111/uk-gov-tenders-buyer-leads``.

Zero-Key Hosted Alternative:
- Agensi Free Skills & GovTech Bundle: https://www.agensi.io/r/GIANGTRNGTRNG
- Local STDIO MCP: npx -y github:truonggiang0111/b2b-market-intel-mcp
- Fresh $29 CSV Packs: https://truonggiang0111.github.io/mcp/b2b-leads-datasets-and-custom-scrapers/
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import html
import json
import os
from typing import Any
import urllib.parse
import urllib.request

CONTRACTS_FINDER_REST = "https://www.contractsfinder.service.gov.uk/api/rest/2"
CONTRACTS_FINDER_OCDS = "https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search"
USER_AGENT = "b2b-ai-mcp-skills-cookbook/1.5"


def _get_json(url: str, *, method: str = "GET", body: bytes | None = None, timeout: float = 15.0) -> Any:
    headers = {"Accept": "application/json", "User-Agent": USER_AGENT}
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def _clean(value: Any) -> str | None:
    if value is None:
        return None
    txt = html.unescape(str(value)).strip()
    return txt or None


def search_uk_gov_tenders_zero_key(keyword: str = "software", limit: int = 5) -> list[dict[str, Any]]:
    """Query UK Contracts Finder REST v2 (with OCDS fallback) using zero API keys."""
    safe_limit = max(1, min(int(limit), 20))
    cleaned_kw = keyword.strip()

    try:
        notice_list: list[dict[str, Any]] = []
        for statuses in (["Open"], None):
            criteria: dict[str, Any] = {"keyword": cleaned_kw}
            if statuses is not None:
                criteria["statuses"] = statuses
            payload = _get_json(
                f"{CONTRACTS_FINDER_REST}/search_notices/json",
                method="POST",
                body=json.dumps({"searchCriteria": criteria, "size": safe_limit}).encode("utf-8"),
            )
            notice_list = payload.get("noticeList") or []
            if notice_list:
                break
        rows: list[dict[str, Any]] = []
        for entry in notice_list[:safe_limit]:
            item = entry.get("item") if isinstance(entry, dict) else None
            if not isinstance(item, dict):
                continue
            nid = str(item.get("id") or "")
            buyer_email = None
            buyer_phone = None
            if nid:
                try:
                    detail = _get_json(f"{CONTRACTS_FINDER_REST}/get_published_notice/json/{nid}")
                    contact = (detail.get("notice") or {}).get("contactDetails") or {}
                    buyer_email = _clean(contact.get("email"))
                    buyer_phone = _clean(contact.get("phone"))
                except Exception:
                    pass
            rows.append(
                {
                    "notice_id": nid,
                    "title": _clean(item.get("title")),
                    "buyer_name": _clean(item.get("organisationName")),
                    "buyer_email": buyer_email,
                    "buyer_phone": buyer_phone,
                    "value_gbp": item.get("valueHigh") or item.get("valueLow") or item.get("awardedValue"),
                    "deadline": item.get("deadlineDate"),
                    "status": item.get("noticeStatus"),
                    "notice_url": f"https://www.contractsfinder.service.gov.uk/Notice/{nid}",
                    "source_api": "contracts-finder-rest-v2",
                }
            )
        if rows:
            return rows
    except Exception:
        pass

    since = (datetime.now(timezone.utc) - timedelta(days=60)).strftime("%Y-%m-%dT%H:%M:%SZ")
    ocds_url = f"{CONTRACTS_FINDER_OCDS}?" + urllib.parse.urlencode(
        {"publishedFrom": since, "stages": "tender", "limit": str(50 if cleaned_kw else safe_limit)}
    )
    ocds = _get_json(ocds_url)
    kw_lower = cleaned_kw.lower()
    fallback_rows: list[dict[str, Any]] = []
    for rel in ocds.get("releases") or []:
        tender = rel.get("tender") or {}
        title = _clean(tender.get("title")) or ""
        desc = _clean(tender.get("description")) or ""
        if kw_lower and kw_lower not in title.lower() and kw_lower not in desc.lower():
            continue
        parties = rel.get("parties") or []
        buyer = next(
            (p for p in parties if "buyer" in (p.get("roles") or []) or "procuringEntity" in (p.get("roles") or [])),
            parties[0] if parties else {},
        )
        contact = buyer.get("contactPoint") or {}
        rel_id = str(rel.get("id") or "")
        notice_uuid = rel_id.rsplit("-", 1)[0] if "-" in rel_id else rel_id
        fallback_rows.append(
            {
                "notice_id": notice_uuid or rel.get("ocid"),
                "title": title,
                "buyer_name": _clean((rel.get("buyer") or {}).get("name")) or _clean(buyer.get("name")),
                "buyer_email": _clean(contact.get("email")),
                "buyer_phone": _clean(contact.get("telephone")),
                "value_gbp": (tender.get("value") or {}).get("amount"),
                "deadline": (tender.get("tenderPeriod") or {}).get("endDate"),
                "status": tender.get("status") or "tender",
                "notice_url": f"https://www.contractsfinder.service.gov.uk/Notice/{notice_uuid}" if notice_uuid else ocds_url,
                "source_api": "contracts-finder-ocds",
            }
        )
        if len(fallback_rows) >= safe_limit:
            break
    return fallback_rows


def enrich_uk_tenders_apify(keywords: list[str], max_items: int = 20, apify_token: str | None = None) -> list[dict[str, Any]]:
    """Run ttyan0111/uk-gov-tenders-buyer-leads via Apify ($5/mo free tier)."""
    token = (apify_token or os.environ.get("APIFY_TOKEN") or "").strip()
    if not token:
        raise RuntimeError("APIFY_TOKEN env var is required for Apify batch enrichment.")

    endpoint = (
        "https://api.apify.com/v2/acts/"
        "ttyan0111~uk-gov-tenders-buyer-leads/run-sync-get-dataset-items?"
        + urllib.parse.urlencode(
            {
                "token": token,
                "fields": "title,stage,buyerName,contactEmail,valueGBP,deadlineDate,cpvCode,noticeUrl,agentSummary",
            }
        )
    )
    return _get_json(
        endpoint,
        method="POST",
        body=json.dumps({"keywords": keywords, "onlyWithEmail": True, "maxItems": max_items}).encode("utf-8"),
        timeout=90.0,
    )


def build_langchain_tools() -> list[Any]:
    """Create LangChain StructuredTool instances when langchain_core is installed."""
    try:
        from langchain_core.tools import StructuredTool  # type: ignore[import-not-found]
    except ImportError:
        return [
            {
                "title": "search_uk_gov_tenders",
                "description": "Search official UK Contracts Finder notices with buyer emails and GBP values (zero API keys).",
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Procurement keyword such as 'software' or 'cloud'."},
                    "limit": {"type": "integer", "default": 5},
                },
                "required": ["keyword"],
            }
        ]

    return [
        StructuredTool.from_function(
            func=search_uk_gov_tenders_zero_key,
            name="search_uk_gov_tenders",
            description="Search official UK Contracts Finder notices with buyer emails, GBP budgets, and notice links.",
        )
    ]


def run_langchain_agent(prompt: str) -> str:
    """Bind UK Contracts Finder tools to ChatOpenAI via LangChain."""
    try:
        from langchain_openai import ChatOpenAI  # type: ignore[import-not-found]
    except ImportError as exc:
        raise RuntimeError(
            "Install `pip install langchain-core langchain-openai` to run --live-langchain."
        ) from exc

    tools = build_langchain_tools()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)
    ai_msg = llm.invoke(prompt)
    tool_outputs = []
    for call in getattr(ai_msg, "tool_calls", []) or []:
        if call["name"] == "search_uk_gov_tenders":
            tool_outputs.append(search_uk_gov_tenders_zero_key(**call["args"]))
    return json.dumps({"ai_tool_calls": getattr(ai_msg, "tool_calls", []), "results": tool_outputs}, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description="LangChain Tool example for UK Gov Contracts Finder buyer leads.")
    parser.add_argument("--keyword", default="cloud", help="UK procurement search keyword.")
    parser.add_argument("--limit", type=int, default=3, help="Max notices to fetch.")
    parser.add_argument("--live-langchain", action="store_true", help="Invoke ChatOpenAI.bind_tools() via LangChain.")
    parser.add_argument("--apify-live", action="store_true", help="Run Apify uk-gov-tenders-buyer-leads (requires APIFY_TOKEN).")
    args = parser.parse_args()

    if args.live_langchain:
        print(run_langchain_agent(f"Find {args.limit} UK public sector {args.keyword} tenders with buyer emails."))
        return

    if args.apify_live:
        print(json.dumps(enrich_uk_tenders_apify([args.keyword], max_items=args.limit), indent=2))
        return

    tools = build_langchain_tools()
    print(f"=== LangChain Tool Definition Ready ({type(tools[0]).__name__}) ===")
    if isinstance(tools[0], dict):
        print(json.dumps(tools, indent=2))

    notices = search_uk_gov_tenders_zero_key(keyword=args.keyword, limit=args.limit)
    print(f"\n=== Zero-Key UK Contracts Finder Live Notices ({len(notices)} rows) ===")
    print(json.dumps(notices, indent=2))


if __name__ == "__main__":
    main()
