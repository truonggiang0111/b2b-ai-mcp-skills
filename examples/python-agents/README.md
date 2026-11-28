# Python AI Agents Cookbook (`OpenAI`, `Claude MCP`, `LangChain`, `CrewAI`)

Runnable **Python 3.10+** agent examples showing how to connect **OpenAI Tool-Calling**, **Anthropic Claude MCP**, **LangChain Tools**, and **CrewAI Agents** to zero-key public B2B endpoints and zero-proxy Apify Cloud Actors (`$5/month` built-in free Apify credit — zero proxy fees).

> **Interactive Browser Guide & Framework Switcher:** [Python, CrewAI, LangChain, OpenAI & Claude B2B Leads Guide (`truonggiang0111.github.io`)](https://truonggiang0111.github.io/mcp/python-crewai-langchain-b2b-leads/)

---

## Quick Index (`4` Runnable Python 3.10+ Scripts)

| Script | AI Framework | Primary Data Source / Endpoint | Zero-Key Demo Mode? |
| :--- | :--- | :--- | :---: |
| [`google_news_rag_agent.py`](./google_news_rag_agent.py) | **OpenAI Tool-Calling** (`tools` + dispatch loop) | `news.google.com` `CBMi`/`AU_yqL` `Fbv4je` decoder + `ttyan0111~google-news-ai-article-extractor` | Yes (stdlib) |
| [`clinical_trials_biotech_agent.py`](./clinical_trials_biotech_agent.py) | **Anthropic Claude MCP** (`mcp_servers` + `tools`) | `clinicaltrials.gov/api/v2/studies` + `ttyan0111~clinical-trials-biotech-leads` | Yes (stdlib) |
| [`uk_tenders_procurement_agent.py`](./uk_tenders_procurement_agent.py) | **LangChain Tool** (`StructuredTool` + `bind_tools`) | UK Contracts Finder REST v2 / OCDS + `ttyan0111~uk-gov-tenders-buyer-leads` | Yes (stdlib) |
| [`shopify_competitor_churn_agent.py`](./shopify_competitor_churn_agent.py) | **CrewAI Agent** (`BaseTool`, `Agent`, `Task`, `Crew`) | `ttyan0111~shopify-app-store-churn-spy` + WordPress.org Plugins 1.2 zero-key probe | Yes (stdlib fallback) |

---

## Run in 5 Seconds (Zero Third-Party Pip Installs Needed for Demo Mode)

Every script defaults to **zero-key live probe mode** using Python's standard library (`urllib.request`, `json`, `base64`, `argparse`):

```bash
python3 examples/python-agents/google_news_rag_agent.py --query "AI startup funding"
python3 examples/python-agents/clinical_trials_biotech_agent.py --condition oncology --limit 3
python3 examples/python-agents/uk_tenders_procurement_agent.py --keyword cloud --limit 3
python3 examples/python-agents/shopify_competitor_churn_agent.py --query klaviyo-email-marketing
```

### Enable Full Agent SDKs & Scaled Apify Cloud Batch Runs

```bash
# Install our zero-dep Python SDK + optional agent frameworks
pip install git+https://github.com/truonggiang0111/b2b-market-intel-python
pip install openai anthropic langchain-core langchain-openai crewai

# Optional: free $5/month Apify credit (https://apify.com/ttyan0111)
export APIFY_TOKEN="apify_api_..."

# Run live framework loops
python3 examples/python-agents/google_news_rag_agent.py --live-openai
python3 examples/python-agents/clinical_trials_biotech_agent.py --live-claude --remote-mcp
python3 examples/python-agents/uk_tenders_procurement_agent.py --live-langchain
python3 examples/python-agents/shopify_competitor_churn_agent.py --live-crew
```

---

## Zero-Key Managed Skills (`3` Free), STDIO MCP & `$29` CSV Storefront

- **Try `3` Free Zero-Key AI Agent Skills via Agensi Affiliate (`$0`):**
  Launch inside Claude Code, Codex CLI, Cursor, or ChatGPT with zero API keys via [**Agensi Storefront (`agensi.io/r/GIANGTRNGTRNG`)**](https://www.agensi.io/r/GIANGTRNGTRNG):
  1. [Google News Real URL Decoder for AI RAG (`$0` Free)](https://www.agensi.io/r/GIANGTRNGTRNG?to=/skills/google-news-real-url-decoder-for-ai-rag&utm_source=python_cookbook)
  2. [UK Direct Employer Hiring Signals — Reed UK (`$0` Free)](https://www.agensi.io/r/GIANGTRNGTRNG?to=/skills/uk-direct-employer-hiring-signals-reed-uk&utm_source=python_cookbook)
  3. [Competitor App Bug & Review Spy — iOS & Play (`$0` Free)](https://www.agensi.io/r/GIANGTRNGTRNG?to=/skills/competitor-app-bug-review-spy-ios-play&utm_source=python_cookbook)
  *(Plus 13 `$5.00` niche skills & 20%–35% off Card / Solana USDC Bundles on [`agensi.io/creators/giang-tr-ng-tr-ng`](https://www.agensi.io/creators/giang-tr-ng-tr-ng).)*
- **Direct `$29` CSV Lead Packs & `$199–$350` Custom Scrapers (24–48h Delivery):**
  Order freshly verified `500–1,000` row B2B CSV/Google Sheets exports (`$29`) or custom Python/Make/n8n/Apify pipelines (`$199–$350` fixed, 20-row free proof first) at the [**`$29` Direct B2B Data Storefront**](https://truonggiang0111.github.io/mcp/b2b-leads-datasets-and-custom-scrapers/).
- **Zero-Key Node.js STDIO MCP Server:**
  ```bash
  npx -y github:truonggiang0111/b2b-market-intel-mcp
  ```
- **Companion Open-Source Repos:** [`b2b-market-intel-python`](https://github.com/truonggiang0111/b2b-market-intel-python) · [`google-sheets-b2b-lead-scraper`](https://github.com/truonggiang0111/google-sheets-b2b-lead-scraper) · [`n8n-nodes-b2b-market-intel`](https://github.com/truonggiang0111/n8n-nodes-b2b-market-intel) · [`b2b-sample-datasets-2026`](https://github.com/truonggiang0111/b2b-sample-datasets-2026)
