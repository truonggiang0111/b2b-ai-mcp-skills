"""Anthropic Claude MCP & Tool-Use example for ClinicalTrials.gov Biotech & PI Leads.

Demonstrates:
1. Zero-key live queries against ClinicalTrials.gov REST API v2
   (``https://clinicaltrials.gov/api/v2/studies``) using compact field extraction.
2. Anthropic Messages API native Remote MCP connector config
   (``https://mcp.apify.com?actors=ttyan0111/clinical-trials-biotech-leads``)
   and local zero-key STDIO MCP config (``npx -y github:truonggiang0111/b2b-market-intel-mcp``).
3. Optional scaled Site-PI email deduplication via Apify ($5/mo free credit).

Zero-Key Hosted Alternative:
- Agensi Free Skills & Biotech Bundle: https://www.agensi.io/r/GIANGTRNGTRNG
- Direct $29 CSV Packs: https://truonggiang0111.github.io/mcp/b2b-leads-datasets-and-custom-scrapers/
"""

from __future__ import annotations

import argparse
import json
import os
from typing import Any
import urllib.parse
import urllib.request

CLINICAL_TRIALS_API = "https://clinicaltrials.gov/api/v2/studies"
USER_AGENT = "b2b-ai-mcp-skills-cookbook/1.5"


def search_clinical_trials_zero_key(
    condition: str,
    *,
    location: str = "United States",
    sponsor_class: str = "INDUSTRY",
    limit: int = 5,
    timeout: float = 15.0,
) -> list[dict[str, Any]]:
    """Query ClinicalTrials.gov API v2 directly with zero API keys."""
    safe_limit = max(1, min(int(limit), 25))
    params: dict[str, str] = {
        "query.cond": condition.strip(),
        "filter.overallStatus": "RECRUITING",
        "pageSize": str(safe_limit),
    }
    if location.strip():
        params["query.locn"] = location.strip()
    if sponsor_class.strip():
        params["filter.advanced"] = f"AREA[LeadSponsorClass]{sponsor_class.strip().upper()}"

    url = f"{CLINICAL_TRIALS_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": USER_AGENT},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8", errors="replace"))

    leads: list[dict[str, Any]] = []
    for study in (payload.get("studies") or [])[:safe_limit]:
        ps = study.get("protocolSection") or {}
        ident = ps.get("identificationModule") or {}
        sponsor = (ps.get("sponsorCollaboratorsModule") or {}).get("leadSponsor") or {}
        design = ps.get("designModule") or {}
        contacts = ps.get("contactsLocationsModule") or {}
        central = contacts.get("centralContacts") or []
        locations = contacts.get("locations") or []
        primary = next((c for c in central if isinstance(c, dict) and c.get("email")), central[0] if central else {})
        nct_id = ident.get("nctId")

        leads.append(
            {
                "nct_id": nct_id,
                "title": ident.get("briefTitle"),
                "sponsor": sponsor.get("name"),
                "sponsor_class": sponsor.get("class"),
                "phases": design.get("phases") or [],
                "enrollment": (design.get("enrollmentInfo") or {}).get("count"),
                "primary_contact_name": primary.get("name"),
                "primary_contact_email": primary.get("email"),
                "locations_count": len(locations),
                "study_url": f"https://clinicaltrials.gov/study/{nct_id}" if nct_id else None,
            }
        )
    return leads


def enrich_biotech_site_pis_apify(
    queries: list[str],
    *,
    location: str = "United States",
    max_trials: int = 10,
    apify_token: str | None = None,
) -> list[dict[str, Any]]:
    """Run ttyan0111/clinical-trials-biotech-leads for deduplicated Site PI contacts."""
    token = (apify_token or os.environ.get("APIFY_TOKEN") or "").strip()
    if not token:
        raise RuntimeError("APIFY_TOKEN env var is required for Apify Site-PI enrichment.")

    endpoint = (
        "https://api.apify.com/v2/acts/"
        "ttyan0111~clinical-trials-biotech-leads/run-sync-get-dataset-items?"
        + urllib.parse.urlencode(
            {
                "token": token,
                "fields": "nctId,briefTitle,leadSponsorName,phasesText,primaryEmail,leadPiSummary,siteContactsCount,studyUrl,agentSummary",
            }
        )
    )
    body = json.dumps(
        {
            "queries": queries,
            "location": location,
            "statuses": ["RECRUITING", "NOT_YET_RECRUITING"],
            "sponsorClass": "INDUSTRY",
            "phases": ["PHASE1", "PHASE2", "PHASE3"],
            "onlyWithEmail": True,
            "includeSiteContacts": True,
            "maxSiteContactsPerTrial": 10,
            "maxTrials": max_trials,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=90.0) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def build_claude_mcp_config(apify_token: str | None = None) -> dict[str, Any]:
    """Return Anthropic Messages API remote MCP + Claude Desktop STDIO configs."""
    token = (apify_token or os.environ.get("APIFY_TOKEN") or "YOUR_APIFY_API_TOKEN").strip()
    return {
        "anthropic_messages_api_mcp_server": {
            "type": "url",
            "url": "https://mcp.apify.com?actors=ttyan0111/clinical-trials-biotech-leads",
            "name": "clinical_trials_biotech_mcp",
            "authorization_token": token,
        },
        "claude_desktop_zero_key_stdio_mcp": {
            "mcpServers": {
                "b2b-market-intel": {
                    "command": "npx",
                    "args": ["-y", "github:truonggiang0111/b2b-market-intel-mcp"],
                }
            }
        },
    }


ANTHROPIC_TOOLS: list[dict[str, Any]] = [
    {
        "name": "search_clinical_trials_zero_key",
        "description": "Search ClinicalTrials.gov REST API v2 for recruiting Industry biotech trials and central sponsor emails (zero API keys).",
        "input_schema": {
            "type": "object",
            "properties": {
                "condition": {"type": "string", "description": "Medical condition, e.g. 'oncology'."},
                "location": {"type": "string", "default": "United States"},
                "limit": {"type": "integer", "default": 5},
            },
            "required": ["condition"],
        },
    }
]


def run_claude_mcp_or_tool_agent(prompt: str, use_remote_mcp: bool = False) -> str:
    """Invoke Anthropic Claude Messages API with zero-key tools or remote Apify MCP."""
    try:
        import anthropic  # type: ignore[import-not-found]
    except ImportError as exc:
        raise RuntimeError("Install anthropic (`pip install anthropic`) to run --live-claude.") from exc

    client = anthropic.Anthropic()
    if use_remote_mcp:
        token = (os.environ.get("APIFY_TOKEN") or "").strip()
        if not token:
            raise RuntimeError("APIFY_TOKEN is required when attaching remote Apify MCP to Claude.")
        resp = client.beta.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            betas=["mcp-client-2025-04-04"],
            mcp_servers=[
                {
                    "type": "url",
                    "url": "https://mcp.apify.com?actors=ttyan0111/clinical-trials-biotech-leads",
                    "name": "clinical_trials_biotech_mcp",
                    "authorization_token": token,
                }
            ],
            messages=[{"role": "user", "content": prompt}],
        )
        return "\n".join(getattr(b, "text", str(b)) for b in resp.content)

    messages: list[dict[str, Any]] = [{"role": "user", "content": prompt}]
    for _ in range(3):
        resp = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            tools=ANTHROPIC_TOOLS,
            messages=messages,
        )
        tool_uses = [b for b in resp.content if getattr(b, "type", "") == "tool_use"]
        if not tool_uses:
            return "\n".join(b.text for b in resp.content if getattr(b, "type", "") == "text")

        messages.append({"role": "assistant", "content": resp.content})
        tool_results = []
        for block in tool_uses:
            data = search_clinical_trials_zero_key(**block.input)
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": json.dumps(data),
                }
            )
        messages.append({"role": "user", "content": tool_results})
    return "Stopped after max Claude tool iterations."


def main() -> None:
    parser = argparse.ArgumentParser(description="Anthropic Claude MCP & ClinicalTrials.gov Biotech Leads example.")
    parser.add_argument("--condition", default="oncology", help="Clinical condition query.")
    parser.add_argument("--limit", type=int, default=3, help="Number of trials to inspect.")
    parser.add_argument("--live-claude", action="store_true", help="Run via Anthropic API (requires ANTHROPIC_API_KEY).")
    parser.add_argument("--remote-mcp", action="store_true", help="Attach remote mcp.apify.com connector in --live-claude.")
    parser.add_argument("--apify-live", action="store_true", help="Run Apify Site-PI enricher (requires APIFY_TOKEN).")
    args = parser.parse_args()

    if args.live_claude:
        print(
            run_claude_mcp_or_tool_agent(
                f"Find {args.limit} recruiting Industry {args.condition} trials with sponsor emails.",
                use_remote_mcp=args.remote_mcp,
            )
        )
        return

    if args.apify_live:
        print(json.dumps(enrich_biotech_site_pis_apify([args.condition], max_trials=args.limit), indent=2))
        return

    print("=== Anthropic Claude MCP Configs (Remote Apify + Zero-Key STDIO) ===")
    print(json.dumps(build_claude_mcp_config(), indent=2))

    leads = search_clinical_trials_zero_key(args.condition, limit=args.limit)
    print(f"\n=== Zero-Key ClinicalTrials.gov API v2 Live Leads ({len(leads)} rows) ===")
    print(json.dumps(leads, indent=2))


if __name__ == "__main__":
    main()
