# `8` Ready-to-Import Make.com Blueprints for B2B Lead Gen, Churn Spy & RAG

Production-ready **Make.com Scenario Blueprints** (`.make.json`) calling Apify **`/run-sync-get-dataset-items`** endpoints (`$5/month` free Apify credit — zero proxy fees) and **Zero-Key Public REST APIs** (`ClinicalTrials.gov v2`, `UK Contracts Finder OCDS`, `WordPress.org Plugins 1.2`, and `Atlassian Marketplace REST v2`).

> **Interactive Browser Previewer & 1-Click Downloader:** [Make.com B2B Lead Blueprints Gallery (`truonggiang0111.github.io`)](https://truonggiang0111.github.io/mcp/make-com-apify-b2b-lead-blueprints/)

---

## 1-Click Make.com Import Instructions (10 Seconds)

1. Download any `.make.json` blueprint from the table below (or use the **Download `.make.json` / Copy Blueprint JSON** buttons in the [Interactive Make.com Gallery](https://truonggiang0111.github.io/mcp/make-com-apify-b2b-lead-blueprints/)).
2. In **Make.com**, open **Scenarios** -> **+ Create a new scenario**.
3. Click **`...` (More)** in the bottom toolbar -> **Import Blueprint** -> select the `.make.json` file and click **Save** (alternatively, press `Esc` on an empty canvas and paste JSON via `Ctrl+V` / `Cmd+V`).
4. For **Zero-Key Blueprints (`#3`, `#4`, `#8`)**, click **Run once** immediately (`$0`, zero API keys needed on Route 1). For **Apify Cloud routes**, replace `YOUR_APIFY_API_TOKEN` in **Module 1 (`SetVariables`)** using your built-in **`$5/mo` free Apify tier** ([apify.com/ttyan0111](https://apify.com/ttyan0111)).

---

## Index of All `8` Make.com Blueprints

| # | Blueprint File | Mode / Auth | Endpoints / Apify Actors | Direct Raw Blueprint URL |
| :- | :--- | :--- | :--- | :--- |
| 1 | [`google-news-real-url-rag.make.json`](./google-news-real-url-rag.make.json) | Apify (`$5/mo` free) | `ttyan0111~google-news-ai-article-extractor/run-sync-get-dataset-items` (decodes `CBMi`/`AU_yqL` -> `url` + LLM RAG text) | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/make/google-news-real-url-rag.make.json` |
| 2 | [`shopify-1star-churn-leads.make.json`](./shopify-1star-churn-leads.make.json) | Apify (`$5/mo` free) | `ttyan0111~shopify-app-store-churn-spy/run-sync-get-dataset-items` (`1★–2★` churn, `mentionedDomains`, `developerEmail`) | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/make/shopify-1star-churn-leads.make.json` |
| 3 | [`clinicaltrials-biotech-pi-leads.make.json`](./clinicaltrials-biotech-pi-leads.make.json) | **Zero-Key Instant** (+ optional Apify PI enrich) | `clinicaltrials.gov/api/v2/studies` + optional `ttyan0111~clinical-trials-biotech-leads/run-sync-get-dataset-items` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/make/clinicaltrials-biotech-pi-leads.make.json` |
| 4 | [`uk-gov-tenders-buyer-emails.make.json`](./uk-gov-tenders-buyer-emails.make.json) | **Zero-Key Instant** (+ optional Apify buyer enrich) | `contractsfinder.service.gov.uk/Published/Notices/OCDS/Search` + optional `ttyan0111~uk-gov-tenders-buyer-leads/run-sync-get-dataset-items` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/make/uk-gov-tenders-buyer-emails.make.json` |
| 5 | [`reed-seek-direct-hiring-leads.make.json`](./reed-seek-direct-hiring-leads.make.json) | Apify (`$5/mo` free) | `ttyan0111~reed-uk-jobs-hiring-signals` (`directEmployerOnly`, IR35) + `ttyan0111~seek-au-nz-jobs-hiring-signals` (GraphQL) | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/make/reed-seek-direct-hiring-leads.make.json` |
| 6 | [`substack-creator-sponsor-leads.make.json`](./substack-creator-sponsor-leads.make.json) | Apify (`$5/mo` free) | `ttyan0111~substack-newsletter-creator-leads/run-sync-get-dataset-items` (`paidNewslettersOnly`, `contactEmail`) | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/make/substack-creator-sponsor-leads.make.json` |
| 7 | [`vscode-chrome-competitor-bug-spy.make.json`](./vscode-chrome-competitor-bug-spy.make.json) | Apify (`$5/mo` free) | `ttyan0111~vscode-cursor-extension-spy` (VS Code + Open-VSX) + `ttyan0111~chrome-web-store-extension-spy` (`developerEmail`) | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/make/vscode-chrome-competitor-bug-spy.make.json` |
| 8 | [`wordpress-atlassian-churn-leads.make.json`](./wordpress-atlassian-churn-leads.make.json) | **Zero-Key Instant** (+ optional Apify enrich) | `api.wordpress.org/plugins/info/1.2/` + `marketplace.atlassian.com/rest/2/addons` + optional `wordpress-plugin-churn-spy` & `atlassian-marketplace-b2b-spy` | `https://raw.githubusercontent.com/truonggiang0111/b2b-ai-mcp-skills/main/workflows/make/wordpress-atlassian-churn-leads.make.json` |

---

## Zero-Key Hosted Skills (3 Free Skills), STDIO MCP & Done-For-You Storefront

- **3 Free Zero-Key AI Agent Skills on Agensi.io (`$0` — Card/USDC Bundles `20%–35%` Off):**
  Start directly on [Giang's Agensi Storefront](https://www.agensi.io/r/GIANGTRNGTRNG) (`https://www.agensi.io/r/GIANGTRNGTRNG`, [direct storefront](https://www.agensi.io/creators/giang-tr-ng-tr-ng)) and try all **3 Free Skills** with zero API keys:
  1. [Google News Real URL Decoder for AI RAG (`$0` Free)](https://www.agensi.io/r/GIANGTRNGTRNG?to=/skills/google-news-real-url-decoder-for-ai-rag&utm_source=make_readme)
  2. [UK Direct Employer Hiring Signals — Reed UK (`$0` Free)](https://www.agensi.io/r/GIANGTRNGTRNG?to=/skills/uk-direct-employer-hiring-signals-reed-uk&utm_source=make_readme)
  3. [Competitor App Bug & Review Spy — iOS & Play (`$0` Free)](https://www.agensi.io/r/GIANGTRNGTRNG?to=/skills/competitor-app-bug-review-spy-ios-play&utm_source=make_readme)
- **Direct `$29` CSV Lead Packs & `$199–$350` Custom Scrapers (24–48h Delivery):**
  Need freshly compiled `500–1,000` row B2B CSV/Google Sheets exports (`$29` fixed) or a bespoke Make.com / Apify / Google Sheets pipeline (`$199–$350` fixed)? Order directly at the [**Direct B2B Data Storefront & Custom Scraper Hub**](https://truonggiang0111.github.io/mcp/b2b-leads-datasets-and-custom-scrapers/).
- **Zero-Key Local STDIO MCP Server (Node 18+):**
  ```bash
  npx -y github:truonggiang0111/b2b-market-intel-mcp
  ```
- **Companion Open-Source Stack:** [`workflows/n8n/` (`16` Templates)](../n8n/README.md) · [`n8n-nodes-b2b-market-intel`](https://github.com/truonggiang0111/n8n-nodes-b2b-market-intel) · [`google-sheets-b2b-lead-scraper`](https://github.com/truonggiang0111/google-sheets-b2b-lead-scraper) · [Apify Store (`@ttyan0111`, `$5/mo` Free Tier)](https://apify.com/ttyan0111)
