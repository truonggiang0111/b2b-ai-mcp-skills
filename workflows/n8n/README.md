# `16` Ready-to-Import `n8n` Workflows for B2B Lead Gen, Churn Spy, RAG & MCP AI Agents

Production-ready **n8n workflow templates** (`.n8n.json`) covering **Zero-Key Public APIs**, **n8n AI Agent MCP Clients (Streamable HTTP & STDIO)**, **1★–2★ Competitor Churn & Data-Bait Outreach**, **Hiring Signals**, **GovTech / ClinicalTrials Leads**, and **Creator / Ad Intelligence**.

Every workflow includes:
- A **`Test Workflow Manually`** (`manualTrigger`) or **`When Chat Message Received`** (`chatTrigger`) node for instant 1-click canvas testing.
- An embedded **Setup & Free Zero-Key Options** `stickyNote` right on the canvas.
- Zero hardcoded secrets (`0` tokens). Zero-Key workflows (`#11`, `#12`, `#13`, `#15`) run out of the box with **`$0` API keys**; Apify-powered workflows run on Apify's **`$5/month` free tier** ([apify.com/ttyan0111](https://apify.com/ttyan0111)) with zero proxy charges.

---

## How to Import in 10 Seconds

1. In **n8n**, create a new workflow -> click **`...` (Menu)** -> **Import from URL...** (or **Import from File...**).
2. Paste any **Direct Raw Import URL** from the index below.
3. Click **Execute Workflow** (via the wired `Test Workflow Manually` trigger) or **Open Chat** for the MCP AI Agent templates.

---

## Index of All `16` `n8n` Workflows

| # | Workflow File | Mode / Auth | Source / Actor / Endpoint | Direct Raw Import URL (`Import from URL`) |
| :- | :--- | :--- | :--- | :--- |
| 1 | [`daily-google-news-ai-rag-digest.n8n.json`](./daily-google-news-ai-rag-digest.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `ttyan0111~google-news-ai-article-extractor` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/daily-google-news-ai-rag-digest.n8n.json` |
| 2 | [`weekly-competitor-app-bug-spy.n8n.json`](./weekly-competitor-app-bug-spy.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `ttyan0111~app-store-play-reviews-spy` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/weekly-competitor-app-bug-spy.n8n.json` |
| 3 | [`weekly-shopify-app-churn-leads.n8n.json`](./weekly-shopify-app-churn-leads.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `ttyan0111~shopify-app-store-churn-spy` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/weekly-shopify-app-churn-leads.n8n.json` |
| 4 | [`daily-uk-au-direct-employer-leads.n8n.json`](./daily-uk-au-direct-employer-leads.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `reed-uk-jobs-hiring-signals` + `seek-au-nz-jobs-hiring-signals` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/daily-uk-au-direct-employer-leads.n8n.json` |
| 5 | [`daily-uk-gov-tenders-alert.n8n.json`](./daily-uk-gov-tenders-alert.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `ttyan0111~uk-gov-tenders-buyer-leads` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/daily-uk-gov-tenders-alert.n8n.json` |
| 6 | [`weekly-vscode-chrome-extension-bugs.n8n.json`](./weekly-vscode-chrome-extension-bugs.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `vscode-cursor-extension-spy` + `chrome-web-store-extension-spy` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/weekly-vscode-chrome-extension-bugs.n8n.json` |
| 7 | [`weekly-podcast-guest-sponsor-outreach.n8n.json`](./weekly-podcast-guest-sponsor-outreach.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `ttyan0111~podcast-host-email-sponsor-spy` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/weekly-podcast-guest-sponsor-outreach.n8n.json` |
| 8 | [`weekly-google-ads-winning-creatives.n8n.json`](./weekly-google-ads-winning-creatives.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `ttyan0111~google-ads-transparency-spy` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/weekly-google-ads-winning-creatives.n8n.json` |
| 9 | [`weekly-substack-paid-creator-leads.n8n.json`](./weekly-substack-paid-creator-leads.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `ttyan0111~substack-newsletter-creator-leads` (paid + direct email + sponsor filter) | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/weekly-substack-paid-creator-leads.n8n.json` |
| 10 | [`daily-substack-viral-notes-ghostwriter.n8n.json`](./daily-substack-viral-notes-ghostwriter.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `ttyan0111~substack-viral-notes-outlier-spy` (`>=3x` outliers + `RUN_SUMMARY.ghostwriterSwipePrompt`) | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/daily-substack-viral-notes-ghostwriter.n8n.json` |
| 11 | [`daily-clinical-trials-biotech-sponsor-leads.n8n.json`](./daily-clinical-trials-biotech-sponsor-leads.n8n.json) | **Zero-Key Instant** (+ optional Apify enrich) | `clinicaltrials.gov/api/v2/studies` + optional `ttyan0111~clinical-trials-biotech-leads` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/daily-clinical-trials-biotech-sponsor-leads.n8n.json` |
| 12 | [`weekly-atlassian-jira-app-churn-leads.n8n.json`](./weekly-atlassian-jira-app-churn-leads.n8n.json) | **Zero-Key Instant** (+ optional Apify enrich) | `marketplace.atlassian.com/rest/2/addons` + optional `ttyan0111~atlassian-marketplace-b2b-spy` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/weekly-atlassian-jira-app-churn-leads.n8n.json` |
| 13 | [`weekly-wordpress-woocommerce-plugin-churn-leads.n8n.json`](./weekly-wordpress-woocommerce-plugin-churn-leads.n8n.json) | **Zero-Key Instant** (+ optional Apify enrich) | `api.wordpress.org/plugins/info/1.2/` + optional `ttyan0111~wordpress-plugin-churn-spy` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/weekly-wordpress-woocommerce-plugin-churn-leads.n8n.json` |
| 14 | [`n8n-ai-agent-streamable-http-mcp-prospecting.n8n.json`](./n8n-ai-agent-streamable-http-mcp-prospecting.n8n.json) | **MCP AI Agent** (`httpStreamable`) | `@n8n/n8n-nodes-langchain.agent` + `mcpClientTool` (`mcp.apify.com` Reed/Shopify/GNews) | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/n8n-ai-agent-streamable-http-mcp-prospecting.n8n.json` |
| 15 | [`n8n-ai-agent-stdio-zero-key-mcp-research.n8n.json`](./n8n-ai-agent-stdio-zero-key-mcp-research.n8n.json) | **Zero-Key MCP AI Agent** (STDIO Bridge) | `mcpClientTool` + `npx -y github:truonggiang0111/b2b-market-intel-mcp` (via `supergateway`) | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/n8n-ai-agent-stdio-zero-key-mcp-research.n8n.json` |
| 16 | [`weekly-competitor-review-databait-outreach-drafter.n8n.json`](./weekly-competitor-review-databait-outreach-drafter.n8n.json) | Schedule + Manual · Apify (`$5/mo` free) | `ttyan0111~app-store-play-reviews-spy` -> `<80`-word Data-Bait cold outreach drafts | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/n8n/weekly-competitor-review-databait-outreach-drafter.n8n.json` |

---

## Companion n8n Node, MCP CLI, Python SDK & Hosted Skills

- **Native n8n Community Node (`usableAsTool: true`, `18` Operations):**
  ```bash
  # Install inside ~/.n8n/nodes
  npm install github:truonggiang0111/n8n-nodes-b2b-market-intel
  ```
  Repo: [truonggiang0111/n8n-nodes-b2b-market-intel](https://github.com/truonggiang0111/n8n-nodes-b2b-market-intel)
- **Zero-Key Node.js STDIO MCP Server (`npx`):**
  ```bash
  npx -y github:truonggiang0111/b2b-market-intel-mcp
  # Optional bridge for n8n mcpClientTool:
  npx -y supergateway --stdio "npx -y github:truonggiang0111/b2b-market-intel-mcp" --outputTransport streamableHttp --port 8000
  ```
- **Python 3.10+ Zero-Dep SDK & CLI:** [truonggiang0111/b2b-market-intel-python](https://github.com/truonggiang0111/b2b-market-intel-python)
- **Hosted Zero-Key Agent Skills & Bundles (`$0`–`$12.99`):** [Agensi.io Storefront](https://www.agensi.io/creators/giang-tr-ng-tr-ng)
- **Cloud Actors (`$5/month` Free Usage Tier):** [apify.com/ttyan0111](https://apify.com/ttyan0111)
