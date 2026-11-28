"""CrewAI Agent example for Shopify 1-Star Churn & Competitor Plugin Spy.

Demonstrates:
1. CrewAI ``BaseTool`` + ``Agent`` + ``Task`` + ``Crew`` integration wired to
   ``ttyan0111/shopify-app-store-churn-spy`` (Apify $5/mo built-in free credit)
   to mine 1-2 star merchant complaints, ``mentionedDomains``, and ``developerEmail``.
2. Zero-key live fallback against ``api.wordpress.org/plugins/info/1.2/`` so
   ``--demo`` works immediately even before setting ``APIFY_TOKEN`` or ``OPENAI_API_KEY``.

Zero-Key Hosted Alternative:
- Agensi Free Skills & E-Commerce Churn Bundle: https://www.agensi.io/r/GIANGTRNGTRNG
- Local STDIO MCP: npx -y github:truonggiang0111/b2b-market-intel-mcp
- Fresh $29 CSV Packs: https://truonggiang0111.github.io/mcp/b2b-leads-datasets-and-custom-scrapers/
"""

from __future__ import annotations

import argparse
import json
import os
from typing import Any
import urllib.parse
import urllib.request

APIFY_SHOPIFY_ENDPOINT = (
    "https://api.apify.com/v2/acts/"
    "ttyan0111~shopify-app-store-churn-spy/run-sync-get-dataset-items"
)
WP_PLUGINS_API = "https://api.wordpress.org/plugins/info/1.2/"
USER_AGENT = "b2b-ai-mcp-skills-cookbook/1.5"


def fetch_shopify_churn_apify(
    queries: list[str],
    *,
    max_apps_per_query: int = 3,
    max_reviews_per_app: int = 15,
    apify_token: str | None = None,
) -> list[dict[str, Any]]:
    """Run ttyan0111/shopify-app-store-churn-spy synchronously ($5/mo free Apify tier)."""
    token = (apify_token or os.environ.get("APIFY_TOKEN") or "").strip()
    if not token:
        raise RuntimeError(
            "APIFY_TOKEN is not set. Create a free $5/mo Apify account at https://apify.com/ttyan0111 "
            "or run with --demo for the zero-key WordPress.org competitor churn probe."
        )

    url = f"{APIFY_SHOPIFY_ENDPOINT}?" + urllib.parse.urlencode(
        {
            "token": token,
            "fields": "name,handle,rating,ratingCount,developerEmail,mentionedDomains,painSignalSummary,appUrl,agentSummary",
        }
    )
    payload = json.dumps(
        {
            "queries": queries,
            "maxAppsPerQuery": max_apps_per_query,
            "includeReviews": True,
            "starRatings": ["1", "2"],
            "sortBy": "newest",
            "maxReviewsPerApp": max_reviews_per_app,
            "onlyWithDeveloperEmail": False,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=90.0) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def fetch_wordpress_churn_zero_key(search_term: str = "woocommerce stripe", limit: int = 3) -> list[dict[str, Any]]:
    """Zero-key public WordPress.org API 1.2 probe showing low-star ratio & support backlog."""
    params = urllib.parse.urlencode(
        {
            "action": "query_plugins",
            "request[search]": search_term,
            "request[per_page]": str(max(1, min(limit, 10))),
            "request[fields][ratings]": "1",
            "request[fields][active_installs]": "1",
            "request[fields][support_threads]": "1",
            "request[fields][support_threads_resolved]": "1",
            "request[fields][homepage]": "1",
        }
    )
    req = urllib.request.Request(
        f"{WP_PLUGINS_API}?{params}",
        headers={"Accept": "application/json", "User-Agent": USER_AGENT},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=15.0) as resp:
        payload = json.loads(resp.read().decode("utf-8", errors="replace"))

    results: list[dict[str, Any]] = []
    for p in (payload.get("plugins") or [])[:limit]:
        ratings = p.get("ratings") or {}
        one_star = int(ratings.get("1", 0)) if isinstance(ratings, dict) else 0
        total_threads = int(p.get("support_threads") or 0)
        resolved = int(p.get("support_threads_resolved") or 0)
        results.append(
            {
                "slug": p.get("slug"),
                "name": p.get("name"),
                "active_installs": p.get("active_installs"),
                "rating_pct": p.get("rating"),
                "one_star_reviews": one_star,
                "unresolved_support_threads": max(0, total_threads - resolved),
                "homepage": p.get("homepage"),
                "rss_1star_url": f"https://wordpress.org/support/plugin/{p.get('slug')}/reviews/feed/?filter=1",
            }
        )
    return results


def build_crewai_components() -> dict[str, Any]:
    """Instantiate CrewAI BaseTool + Agent + Task when crewai is installed."""
    try:
        from crewai import Agent, Crew, Task  # type: ignore[import-not-found]
        from crewai.tools import BaseTool  # type: ignore[import-not-found]
    except ImportError:
        return {
            "installed": False,
            "agent_role": "B2B Churn & Competitive Intelligence Analyst",
            "tool_name": "shopify_app_churn_spy",
            "apify_actor": "ttyan0111/shopify-app-store-churn-spy",
            "zero_key_fallback": "api.wordpress.org/plugins/info/1.2/",
        }

    class ShopifyChurnSpyTool(BaseTool):  # type: ignore[misc]
        name: str = "shopify_app_churn_spy"
        description: str = (
            "Extract Shopify App Store 1-star & 2-star churn reviews, complaining merchant domains, "
            "and developer emails via ttyan0111/shopify-app-store-churn-spy."
        )

        def _run(self, query: str) -> str:
            if os.environ.get("APIFY_TOKEN"):
                rows = fetch_shopify_churn_apify([query])
            else:
                rows = fetch_wordpress_churn_zero_key(query)
            return json.dumps(rows, indent=2)

    tool = ShopifyChurnSpyTool()
    analyst = Agent(
        role="B2B Churn & Competitive Intelligence Analyst",
        goal="Surface high-intent ecommerce merchants leaving 1-star reviews due to crashes or billing friction.",
        backstory="Specializes in product-led B2B outbound using verified review pain signals.",
        tools=[tool],
        verbose=True,
    )
    task = Task(
        description="Inspect competitor 1-star churn signals for '{topic}' and draft 3 crisp data-bait outreach angles.",
        expected_output="A bulleted JSON/Markdown brief listing affected store domains, pain tags, and outreach angles.",
        agent=analyst,
    )
    crew = Crew(agents=[analyst], tasks=[task], verbose=True)
    return {"installed": True, "crew": crew, "agent": analyst, "task": task, "tool": tool}


def main() -> None:
    parser = argparse.ArgumentParser(description="CrewAI Agent example for Shopify & WooCommerce 1-Star Churn Spy.")
    parser.add_argument("--query", default="klaviyo-email-marketing", help="Shopify app query or keyword.")
    parser.add_argument("--live-crew", action="store_true", help="Run CrewAI kickoff (requires crewai + LLM API key).")
    parser.add_argument("--apify-live", action="store_true", help="Call Shopify Churn Apify actor directly (requires APIFY_TOKEN).")
    args = parser.parse_args()

    if args.live_crew:
        bundle = build_crewai_components()
        if not bundle.get("installed"):
            raise RuntimeError("Install CrewAI (`pip install crewai`) to run --live-crew.")
        print(bundle["crew"].kickoff(inputs={"topic": args.query}))
        return

    if args.apify_live:
        rows = fetch_shopify_churn_apify([args.query], max_apps_per_query=2, max_reviews_per_app=10)
        print(json.dumps(rows, indent=2))
        return

    bundle = build_crewai_components()
    print("=== CrewAI Agent Blueprint ===")
    print(
        json.dumps(
            {
                "crewai_installed": bundle["installed"],
                "role": "B2B Churn & Competitive Intelligence Analyst",
                "primary_apify_endpoint": APIFY_SHOPIFY_ENDPOINT,
                "sample_payload": {"queries": [args.query], "starRatings": ["1", "2"], "maxAppsPerQuery": 3},
            },
            indent=2,
        )
    )

    wp_rows = fetch_wordpress_churn_zero_key("woocommerce stripe", limit=3)
    print(f"\n=== Zero-Key Companion Probe (WordPress.org Plugins 1.2 — {len(wp_rows)} rows) ===")
    print(json.dumps(wp_rows, indent=2))


if __name__ == "__main__":
    main()
