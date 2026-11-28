"""OpenAI Tool-Calling example for Google News Real-URL decoding & AI RAG.

Demonstrates:
1. Zero-key offline protobuf decoding for legacy ``CBMi`` Google News links
   and live ``DotsSplashUi`` ``Fbv4je`` signed exchange for 2024-2026 ``AU_yqL`` links.
2. Optional scaled batch extraction + clean Markdown RAG bodies via Apify
   ``ttyan0111/google-news-ai-article-extractor`` ($5/month built-in free credit).
3. OpenAI Chat Completions tool-calling schema & dispatch loop.

Zero-key Hosted Alternative:
- Agensi Free Skill ($0): https://www.agensi.io/r/GIANGTRNGTRNG
- Local STDIO MCP: npx -y github:truonggiang0111/b2b-market-intel-mcp
- Fresh $29 CSV Packs: https://truonggiang0111.github.io/mcp/b2b-leads-datasets-and-custom-scrapers/
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
from typing import Any
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
GNEWS_TOKEN_RE = re.compile(r"/(?:rss/)?(?:articles|read)/([A-Za-z0-9_-]+)")
SG_RE = re.compile(r'data-n-a-sg="([^"]+)"')
TS_RE = re.compile(r'data-n-a-ts="([^"]+)"')
GARTURLRES_RE = re.compile(r'\[\s*\\"garturlres\\"\s*,\s*\\"(https?:[^"\\]+)\\"')


def _http_text(
    url: str,
    *,
    method: str = "GET",
    data: bytes | None = None,
    headers: dict[str, str] | None = None,
    timeout: float = 12.0,
) -> str:
    req_headers = {"User-Agent": USER_AGENT}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, data=data, headers=req_headers, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _read_varint(buf: bytes, offset: int) -> tuple[int, int] | None:
    value = 0
    shift = 0
    pos = offset
    while pos < len(buf):
        byte = buf[pos]
        pos += 1
        value |= (byte & 0x7F) << shift
        if (byte & 0x80) == 0:
            return value, pos
        shift += 7
        if shift > 35:
            return None
    return None


def _extract_legacy_protobuf_url(token: str) -> str | None:
    try:
        padded = token + "=" * (-len(token) % 4)
        buf = base64.urlsafe_b64decode(padded.encode("ascii"))
    except Exception:
        return None
    offset = 0
    while offset < len(buf):
        tag_info = _read_varint(buf, offset)
        if tag_info is None:
            break
        tag, offset = tag_info
        wire_type = tag & 0x07
        if wire_type == 0:
            varint_info = _read_varint(buf, offset)
            if varint_info is None:
                break
            _, offset = varint_info
        elif wire_type == 2:
            len_info = _read_varint(buf, offset)
            if len_info is None:
                break
            length, start = len_info
            end = start + length
            if end > len(buf):
                break
            text = buf[start:end].decode("utf-8", errors="ignore")
            offset = end
            if re.match(r"^https?://", text, re.IGNORECASE):
                return text
        else:
            break
    return None


def decode_google_news_url(url: str, timeout: float = 10.0) -> dict[str, Any]:
    """Decode a news.google.com/rss/articles/... URL with zero API keys."""
    match = GNEWS_TOKEN_RE.search(urllib.parse.urlparse(url.strip()).path)
    if not match:
        return {"source_url": url, "decoded_url": url, "method": "passthrough"}

    token = match.group(1)
    legacy_url = _extract_legacy_protobuf_url(token)
    if legacy_url:
        return {
            "source_url": url,
            "decoded_url": legacy_url,
            "method": "legacy-protobuf-base64",
        }

    sg: str | None = None
    ts: str | None = None
    for endpoint in (
        f"https://news.google.com/articles/{token}",
        f"https://news.google.com/rss/articles/{token}",
    ):
        html = _http_text(
            endpoint,
            headers={"Accept": "text/html,application/xhtml+xml"},
            timeout=timeout,
        )
        sg_m, ts_m = SG_RE.search(html), TS_RE.search(html)
        if sg_m and ts_m:
            sg, ts = sg_m.group(1), ts_m.group(1)
            break
    if not sg or not ts:
        raise RuntimeError("Could not extract data-n-a-sg / data-n-a-ts from Google News splash HTML")

    inner = [
        "garturlreq",
        [["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1, None, None, None, None, None, 0, 1], "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0],
        token,
        int(ts),
        sg,
    ]
    envelope = [[["Fbv4je", json.dumps(inner), None, "generic"]]]
    body = urllib.parse.urlencode({"f.req": json.dumps(envelope)}).encode("utf-8")
    raw = _http_text(
        "https://news.google.com/_/DotsSplashUi/data/batchexecute?rpcids=Fbv4je",
        method="POST",
        data=body,
        headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Referer": "https://news.google.com/",
        },
        timeout=timeout,
    )
    found = GARTURLRES_RE.search(raw)
    if not found:
        raise RuntimeError("Missing garturlres URL in Fbv4je batchexecute response")

    return {
        "source_url": url,
        "decoded_url": str(json.loads(f'"{found.group(1)}"')),
        "method": "batchexecute-Fbv4je",
    }


def fetch_google_news_rss_sample(query: str, limit: int = 3) -> list[dict[str, str]]:
    """Fetch live RSS items from Google News (zero API keys)."""
    rss_url = (
        "https://news.google.com/rss/search?"
        + urllib.parse.urlencode({"q": query, "hl": "en-US", "gl": "US", "ceid": "US:en"})
    )
    xml_text = _http_text(rss_url, headers={"Accept": "application/rss+xml,application/xml"})
    root = ET.fromstring(xml_text)
    items: list[dict[str, str]] = []
    for item in root.findall("./channel/item")[:limit]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if title and link:
            items.append({"title": title, "google_news_url": link})
    return items


def batch_google_news_rag_apify(
    queries: list[str],
    max_articles_per_query: int = 10,
    apify_token: str | None = None,
) -> list[dict[str, Any]]:
    """Run ttyan0111/google-news-ai-article-extractor via Apify Sync REST API ($5/mo free tier)."""
    token = (apify_token or os.environ.get("APIFY_TOKEN") or "").strip()
    if not token:
        raise RuntimeError("APIFY_TOKEN env var is required for scaled Apify batch extraction.")

    endpoint = (
        "https://api.apify.com/v2/acts/"
        "ttyan0111~google-news-ai-article-extractor/run-sync-get-dataset-items?"
        + urllib.parse.urlencode(
            {
                "token": token,
                "fields": "title,url,urlDecoded,sourceName,publishedAt,marketSignals,agentSummary",
            }
        )
    )
    payload = json.dumps(
        {
            "queries": queries,
            "language": "en-US",
            "timeRange": "7d",
            "decodeSourceUrls": True,
            "extractFullArticle": True,
            "maxArticlesPerQuery": max_articles_per_query,
        }
    ).encode("utf-8")
    raw = _http_text(
        endpoint,
        method="POST",
        data=payload,
        headers={"Content-Type": "application/json"},
        timeout=90.0,
    )
    return json.loads(raw)


OPENAI_TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "decode_google_news_url",
            "description": "Decode an opaque news.google.com/rss/articles/... wrapper into the real publisher URL (zero API keys).",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Full Google News RSS article URL."},
                },
                "required": ["url"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "batch_google_news_rag_apify",
            "description": "Run ttyan0111/google-news-ai-article-extractor for decoded publisher URLs, full RAG Markdown, and PR tags.",
            "parameters": {
                "type": "object",
                "properties": {
                    "queries": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Google News search topics, e.g. ['AI startup funding'].",
                    },
                    "max_articles_per_query": {"type": "integer", "default": 10},
                },
                "required": ["queries"],
            },
        },
    },
]


def dispatch_tool(name: str, arguments: dict[str, Any]) -> Any:
    if name == "decode_google_news_url":
        return decode_google_news_url(str(arguments["url"]))
    if name == "batch_google_news_rag_apify":
        return batch_google_news_rag_apify(
            queries=[str(q) for q in arguments["queries"]],
            max_articles_per_query=int(arguments.get("max_articles_per_query", 10)),
        )
    raise ValueError(f"Unsupported tool: {name}")


def run_openai_agent(prompt: str, model: str = "gpt-4o-mini") -> str:
    """Execute an OpenAI Chat Completions tool-calling loop."""
    try:
        from openai import OpenAI  # type: ignore[import-not-found]
    except ImportError as exc:
        raise RuntimeError("Install openai (`pip install openai`) to run --live-openai.") from exc

    client = OpenAI()
    messages: list[dict[str, Any]] = [
        {"role": "system", "content": "You are a concise AI news RAG analyst. Use tools to resolve real publisher URLs."},
        {"role": "user", "content": prompt},
    ]

    for _ in range(4):
        resp = client.chat.completions.create(model=model, messages=messages, tools=OPENAI_TOOLS)
        msg = resp.choices[0].message
        if not msg.tool_calls:
            return msg.content or ""

        messages.append(msg.model_dump(exclude_none=True))
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments or "{}")
            result = dispatch_tool(call.function.name, args)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": json.dumps(result),
                }
            )
    return "Stopped after max tool iterations."


def main() -> None:
    parser = argparse.ArgumentParser(description="OpenAI Tool-Calling example for Google News Real-URL RAG.")
    parser.add_argument("--query", default="AI startup Series A funding", help="Google News RSS topic for --demo.")
    parser.add_argument("--url", default="", help="Optional news.google.com/rss/articles/... URL to decode directly.")
    parser.add_argument("--live-openai", action="store_true", help="Call OpenAI API (requires openai + OPENAI_API_KEY).")
    parser.add_argument("--apify-live", action="store_true", help="Run batch Apify actor (requires APIFY_TOKEN).")
    args = parser.parse_args()

    if args.live_openai:
        prompt = f"Decode and summarize top Google News links for query: {args.query}"
        if args.url:
            prompt = f"Decode this Google News URL and inspect the destination domain: {args.url}"
        print(run_openai_agent(prompt))
        return

    if args.apify_live:
        rows = batch_google_news_rag_apify([args.query], max_articles_per_query=5)
        print(json.dumps(rows, indent=2))
        return

    print("=== OpenAI Tool Schemas (ready for client.chat.completions.create(tools=OPENAI_TOOLS)) ===")
    print(json.dumps([t["function"]["name"] for t in OPENAI_TOOLS], indent=2))

    if args.url:
        decoded = decode_google_news_url(args.url)
        print("\n=== Zero-Key Direct URL Decode ===")
        print(json.dumps(decoded, indent=2))
        return

    rss_items = fetch_google_news_rss_sample(args.query, limit=2)
    decoded_items = []
    for item in rss_items:
        resolved = decode_google_news_url(item["google_news_url"])
        decoded_items.append({"title": item["title"], **resolved})
    print(f"\n=== Zero-Key Live RSS + Fbv4je Decode ({len(decoded_items)} items) ===")
    print(json.dumps(decoded_items, indent=2))


if __name__ == "__main__":
    main()
