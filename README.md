# B2B Market Intel MCP Servers, Agent Skills (`SKILL.md`) & `n8n` Workflows

[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-io.github.truonggiang0111-10b981?style=flat-square)](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.truonggiang0111)
[![B2B Market Intel Suite MCP connector](https://glama.ai/mcp/connectors/io.github.truonggiang0111/b2b-market-intel-mcp/badges/score.svg)](https://glama.ai/mcp/connectors/io.github.truonggiang0111/b2b-market-intel-mcp)
[![Apify Profile](https://img.shields.io/badge/Apify%20Store-ttyan0111-2563eb?style=flat-square)](https://apify.com/ttyan0111)
[![Agensi.io Storefront](https://img.shields.io/badge/Agensi.io-6%20Live%20Skills-0f172a?style=flat-square)](https://www.agensi.io/creators/giang-tr-ng-tr-ng)
[![Agent Skills](https://img.shields.io/badge/skills.sh-Compatible-6366f1?style=flat-square)](#-2-install-portable-agent-skills-claude-code--cursor--codex)
[![llms.txt](https://img.shields.io/badge/AI%20Index-llms--full.txt-059669?style=flat-square)](./llms-full.txt)

Production-tested **MCP endpoints**, portable **`SKILL.md` playbooks**, and **`n8n` JSON templates** for AI Agents, B2B growth teams, recruiters, and RAG developers. Powered by lightweight zero-proxy cloud endpoints on Apify (**new Apify accounts receive `$5/month` in free usage — try all tools at `$0` out-of-pocket**).

---

## Included Tools & Live Store Links

| Tool / MCP Namespace | What Problem It Solves | Zero-Proxy? | Pay-per-Event Pricing | Live Store & MCP Endpoint |
| :--- | :--- | :---: | :--- | :--- |
| **Google News Real-URL AI Extractor** (`io.github.truonggiang0111/google-news-real-url-mcp`) | Decodes opaque `news.google.com/rss/articles/...` wrappers -> **real publisher URLs**, clean LLM/RAG markdown, `og:image`, and PR tags (`funding`, `launches`, `layoffs`) | Yes | `$0.004` + `$1.00/1k` articles + `$1.80/1k` full text | [Apify Store](https://apify.com/ttyan0111/google-news-ai-article-extractor) |
| **Reed.co.uk Jobs & Direct IR35 Signals** (`io.github.truonggiang0111/reed-uk-jobs-mcp`) | Extracts UK jobs with `direct=True` employer verification, strips `~48%` bootcamp/training ads, normalizes GBP pay, and detects **Outside/Inside IR35** | Yes | `$0.008` + `$1.50/1k` jobs + `$2.00/1k` details | [Apify Store](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals) |
| **Seek AU & NZ Jobs GraphQL Signals** (`io.github.truonggiang0111/seek-au-nz-jobs-mcp`) | Queries `seek.com.au` & `seek.co.nz` via native JSON + GraphQL (bypassing HTML `403` blocks), extracting company industry, headcount & agency flags | Yes | `$0.008` + `$1.50/1k` jobs + `$2.00/1k` GraphQL | [Apify Store](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals) |
| **App Store + Play Reviews Bug Spy** (`io.github.truonggiang0111/app-reviews-bug-spy-mcp`) | Unified iOS + Android schema by app name or ID; native Google Play server-side star filter + automated `crash_bug` / `billing_subscription` tags | Yes | `$0.005` + `$0.005/app` + `$1.20/1k` reviews | [Apify Store](https://apify.com/ttyan0111/app-store-play-reviews-spy) |
| **Google Ads Transparency & EU Spend** (`io.github.truonggiang0111/google-ads-transparency-mcp`) | Extracts Search/Display/YouTube creatives, `minDaysActive` Winning Ads filter, and EU DSA impression reach stats | Hybrid | `$0.003` + `$1.50/1k` ads + `$1.50/1k` details | [Apify Store](https://apify.com/ttyan0111/google-ads-transparency-spy) |
| **Substack Creator Leads** *(tonight `22:00+07`)* | Direct creator emails, subscriber tiers, paid pricing plans & post engagement | Yes | `$0.006` + `$2.00/1k` pubs | [Skill Guide](./skills/substack-creator-leads/SKILL.md) |
| **Chrome Web Store Spy** *(tonight `22:00+07`)* | Developer support emails, install counts, ratings & negative review pain tags | Yes | `$0.006` + `$2.00/1k` ext | [Skill Guide](./skills/chrome-web-store-spy/SKILL.md) |
| **Shopify App Store 1★ Churn & Dev Emails** *(tonight `22:00+07`)* | SSR `1★–2★` churn reviews, complaining merchant store names, pricing plans & developer support emails | Yes | `$0.006` + `$2.00/1k` apps + `$1.20/1k` reviews | [Skill Guide](./skills/shopify-app-store-churn-spy/SKILL.md) |
| **Apple Podcasts Host Emails & Sponsors** *(tonight `22:00+07`)* | Direct `<itunes:email>` from bounded 400 KB RSS XML streams, non-podfaded active filter & sponsor domains | Yes | `$0.006` + `$2.50/1k` leads + `$1.50/1k` RSS | [Skill Guide](./skills/podcast-host-email-sponsor-spy/SKILL.md) |
| **VS Code & Open-VSX Extension Spy** *(tonight `22:00+07`)* | VS Code Marketplace + Open-VSX (Cursor/Windsurf) combined installs, verified domains, GitHub repos & 1–3★ bug reviews | Yes | `$0.006` + `$2.00/1k` ext + `$1.20/1k` reviews | [Skill Guide](./skills/vscode-cursor-extension-spy/SKILL.md) |
| **Substack Viral Notes Outlier & Hook Spy** *(queued public)* | Weighted Viral Score (`Likes + 3×Replies + 5×Restacks`), `>= 2.0x` outlier detection, peak UTC hour & Ghostwriter Swipe prompts | Yes | `$0.005` + `$1.50/1k` notes + `$0.003/creator` | [Skill Guide](./skills/substack-viral-notes-outlier-spy/SKILL.md) |

---

## 1. Connect in 10 Seconds via Remote MCP (Claude Desktop, Cursor, VS Code, Codex)

Expose the entire 5-tool B2B suite (`io.github.truonggiang0111/b2b-market-intel-mcp`) directly inside your AI client:

```json
{
  "mcpServers": {
    "b2b-market-intel": {
      "url": "https://mcp.apify.com?actors=ttyan0111/reed-uk-jobs-hiring-signals,ttyan0111/seek-au-nz-jobs-hiring-signals,ttyan0111/app-store-play-reviews-spy,ttyan0111/google-ads-transparency-spy,ttyan0111/google-news-ai-article-extractor",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_API_TOKEN"
      }
    }
  }
}
```

Every Actor returns two AI-optimized artifacts to keep LLM context lightweight:
1. Per-item **`agentSummary`** — clean single-line summary you can fetch with `fields=agentSummary,...` via `get-dataset-items`.
2. Key-Value Store **`RUN_SUMMARY`** — aggregate statistics (`topEmployers`, `painSignalCounts`, `winningAdsCount`, `decodedUrlsCount`) ready in one read.

---

## 2. Install Portable Agent Skills (Claude Code / Cursor / Codex)

Install individual playbooks into your coding agent with the open `skills` CLI:

```bash
# Install all B2B & RAG skills from this repository
npx skills add truonggiang0111/b2b-ai-mcp-skills

# Or install a single focused skill
npx skills add truonggiang0111/b2b-ai-mcp-skills --skill google-news-real-url-rag
```

---

## 2b. Zero-Key Managed Execution via Agensi.io (`https://mcp.agensi.io/mcp/auth`)

Prefer **zero Apify API keys** inside Claude Code, Codex CLI, Cursor, or ChatGPT? Connect [Agensi MCP (`https://mcp.agensi.io/mcp/auth`)](https://www.agensi.io/creators/giang-tr-ng-tr-ng) — **`6/6` packaged skills are Live** on [Giang's Agensi Storefront](https://www.agensi.io/creators/giang-tr-ng-tr-ng):

| Agensi Listing | Tier / Pricing | Direct Marketplace Link |
| :--- | :--- | :--- |
| **Google News Real URL Decoder for AI RAG** | **Free (`$0`)** | [Open on Agensi](https://www.agensi.io/skills/google-news-real-url-decoder-for-ai-rag) |
| **UK Direct Employer Hiring Signals (Reed UK)** | **Free (`$0`)** | [Open on Agensi](https://www.agensi.io/skills/uk-direct-employer-hiring-signals-reed-uk) |
| **Competitor App Bug & Review Spy (iOS & Play)** | **Free (`$0`)** | [Open on Agensi](https://www.agensi.io/skills/competitor-app-bug-review-spy-ios-play) |
| **AU/NZ Direct Employer Hiring Signals (Seek)** | **`$5.00`** One-time | [Open on Agensi](https://www.agensi.io/skills/au-nz-direct-employer-hiring-signals-seek) |
| **Competitor Google Ads Transparency & Funnel Spy** | **`$5.00`** One-time | [Open on Agensi](https://www.agensi.io/skills/competitor-google-ads-transparency-funnel-spy) |
| **B2B Market & Hiring Intelligence 5-in-1 Pack** | **`$7.99`** (`-20%` Launch Deal -> **`$6.39`**) | [Open on Agensi](https://www.agensi.io/skills/b2b-market-hiring-intelligence-5-in-1-pack) |
| **Bundle: B2B Hiring & Competitor Ad Spy Bundle** | **`$7.99`** (Save `20%` vs `$10.00`) | [Open Bundle](https://www.agensi.io/bundles/b2b-hiring-competitor-ad-spy-bundle) |

> Full single-file AI ingestion spec (inputs, outputs, `RUN_SUMMARY` keys, and all 30 task endpoints): [`llms.txt`](./llms.txt) · [`llms-full.txt`](./llms-full.txt)

---

## 3. Ready-to-Import `n8n` Workflows

Import these JSON files directly into **n8n** and swap in your Apify token (`$5/month` free credit covers dozens of scheduled runs):

- [`workflows/n8n/weekly-competitor-app-bug-spy.n8n.json`](./workflows/n8n/weekly-competitor-app-bug-spy.n8n.json) — Weekly `1★–2★` competitor review & crash-bug digest across iOS & Android.
- [`workflows/n8n/daily-uk-au-direct-employer-leads.n8n.json`](./workflows/n8n/daily-uk-au-direct-employer-leads.n8n.json) — Daily UK (`Reed.co.uk`) + AU (`Seek.com.au`) direct-employer hiring leads merged into one pipeline.
- [`workflows/n8n/weekly-google-ads-winning-creatives.n8n.json`](./workflows/n8n/weekly-google-ads-winning-creatives.n8n.json) — Weekly tracker of competitor ads running `30+` days + EU DSA reach metrics.

---

## 3b. 30 Ready-to-Run Use-Case Tasks (Apify Store + AI `.md` Endpoints)

Each task runs pre-configured B2B/RAG parameters on Apify Cloud and exposes a clean `.md` spec for AI agents (`6` tasks per Actor):

| Niche | Published Use-Case Landing Pages (`Web` + `.md`) |
| :--- | :--- |
| **Reed.co.uk (UK)** | [UK Direct Python](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/uk-direct-employer-python-jobs) ([.md](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/uk-direct-employer-python-jobs.md)) · [Outside IR35 Contracts](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/outside-ir35-uk-contract-tech-jobs) ([.md](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/outside-ir35-uk-contract-tech-jobs.md)) · [Remote Direct Engineers](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/uk-remote-software-engineer-hiring-leads) ([.md](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/uk-remote-software-engineer-hiring-leads.md)) · [UK AI & ML Direct Jobs](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/uk-ai-machine-learning-direct-employer-jobs) ([.md](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/uk-ai-machine-learning-direct-employer-jobs.md)) · [Cybersecurity Outside IR35](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/uk-cybersecurity-contract-outside-ir35-jobs) ([.md](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/uk-cybersecurity-contract-outside-ir35-jobs.md)) · [Manchester Regional Tech](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/manchester-birmingham-uk-tech-hiring-signals) ([.md](https://apify.com/ttyan0111/reed-uk-jobs-hiring-signals/examples/manchester-birmingham-uk-tech-hiring-signals.md)) |
| **Seek (AU & NZ)** | [Sydney Direct Software](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/sydney-direct-employer-software-jobs) ([.md](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/sydney-direct-employer-software-jobs.md)) · [Remote AU Signals](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/australia-remote-tech-jobs-company-signals) ([.md](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/australia-remote-tech-jobs-company-signals.md)) · [NZ Direct Leads](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/new-zealand-direct-employer-hiring-leads) ([.md](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/new-zealand-direct-employer-hiring-leads.md)) · [Melbourne Direct Tech](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/melbourne-brisbane-direct-employer-tech-jobs) ([.md](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/melbourne-brisbane-direct-employer-tech-jobs.md)) · [AU Data & AI Hiring](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/australia-data-ai-engineer-hiring-signals) ([.md](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/australia-data-ai-engineer-hiring-signals.md)) · [AU Mining & Engineering](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/australia-mining-engineering-direct-hiring-leads) ([.md](https://apify.com/ttyan0111/seek-au-nz-jobs-hiring-signals/examples/australia-mining-engineering-direct-hiring-leads.md)) |
| **App Store + Play** | [1★–2★ Competitor Bugs](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/competitor-app-1-star-bug-complaints) ([.md](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/competitor-app-1-star-bug-complaints.md)) · [Billing Churn Audit](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/ios-android-billing-churn-review-audit) ([.md](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/ios-android-billing-churn-review-audit.md)) · [US & UK Benchmark](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/multi-country-mobile-app-sentiment-benchmark) ([.md](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/multi-country-mobile-app-sentiment-benchmark.md)) · [Fintech 1★ Audit](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/fintech-banking-app-1-star-bug-audit) ([.md](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/fintech-banking-app-1-star-bug-audit.md)) · [AI Mobile Churn Spy](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/ai-chatbot-mobile-app-user-churn-complaints) ([.md](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/ai-chatbot-mobile-app-user-churn-complaints.md)) · [Update Regression Bugs](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/competitor-app-latest-version-regression-bugs) ([.md](https://apify.com/ttyan0111/app-store-play-reviews-spy/examples/competitor-app-latest-version-regression-bugs.md)) |
| **Google Ads Spy** | [Winning Ads (30+ Days)](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/competitor-winning-google-ads-30-days) ([.md](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/competitor-winning-google-ads-30-days.md)) · [EU DSA Reach Audit](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/eu-dsa-competitor-ad-reach-spend-audit) ([.md](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/eu-dsa-competitor-ad-reach-spend-audit.md)) · [YouTube Video Ads](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/youtube-video-ad-creatives-competitor-spy) ([.md](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/youtube-video-ad-creatives-competitor-spy.md)) · [B2B SaaS Search Ads](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/b2b-saas-competitor-google-search-ads-spy) ([.md](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/b2b-saas-competitor-google-search-ads-spy.md)) · [Ecommerce D2C Ads](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/ecommerce-d2c-winning-ads-longevity-tracker) ([.md](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/ecommerce-d2c-winning-ads-longevity-tracker.md)) · [Europe DE/FR Reach](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/uk-germany-france-advertiser-spend-reach-spy) ([.md](https://apify.com/ttyan0111/google-ads-transparency-spy/examples/uk-germany-france-advertiser-spend-reach-spy.md)) |
| **Google News RAG** | [Decode RSS Links](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/decode-google-news-rss-real-publisher-urls) ([.md](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/decode-google-news-rss-real-publisher-urls.md)) · [AI Funding RAG](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/ai-startup-funding-news-full-text-rag) ([.md](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/ai-startup-funding-news-full-text-rag.md)) · [Layoffs & Launches PR](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/competitor-pr-layoffs-launches-news-monitor) ([.md](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/competitor-pr-layoffs-launches-news-monitor.md)) · [M&A & CXO Hires](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/mergers-acquisitions-executive-hiring-news-rag) ([.md](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/mergers-acquisitions-executive-hiring-news-rag.md)) · [Cybersecurity Breaches](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/cybersecurity-breach-incident-news-real-urls) ([.md](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/cybersecurity-breach-incident-news-real-urls.md)) · [Fintech & Crypto Reg](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/fintech-crypto-regulatory-news-llm-digest) ([.md](https://apify.com/ttyan0111/google-news-ai-article-extractor/examples/fintech-crypto-regulatory-news-llm-digest.md)) |

---

## 4. Quick REST Example (Python & Node.js)

### Node.js (`fetch`) — Decode `news.google.com` Wrapper URLs to Real Articles

```js
const token = process.env.APIFY_TOKEN;
const res = await fetch(
  "https://api.apify.com/v2/acts/ttyan0111~google-news-ai-article-extractor/run-sync-get-dataset-items?token=" + token,
  {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      queries: ["OpenAI funding"],
      language: "en-US",
      timeRange: "7d",
      decodeSourceUrls: true,
      extractFullArticle: true,
      maxArticlesPerQuery: 5
    })
  }
);
const articles = await res.json();
console.log(articles.map(a => ({ title: a.title, realUrl: a.realUrl, summary: a.agentSummary })));
```

### Python (`requests`) — UK Direct-Employer Jobs Without Bootcamps

```python
import os, requests

resp = requests.post(
    "https://api.apify.com/v2/acts/ttyan0111~reed-uk-jobs-hiring-signals/run-sync-get-dataset-items",
    params={"token": os.environ["APIFY_TOKEN"]},
    json={
        "keywords": "Python Developer",
        "location": "London",
        "directEmployerOnly": True,
        "excludeTrainingCourses": True,
        "maxJobs": 10,
    },
    timeout=60,
)
for job in resp.json():
    print(job["agentSummary"], "->", job["jobUrl"])
```

---

## License

MIT — skills, MCP manifests (`server.json`), and `n8n` workflows are open-source. Hosted cloud execution runs serverlessly on [Apify (`ttyan0111`)](https://apify.com/ttyan0111).
