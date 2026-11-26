# B2B Market Intel MCP Servers, Agent Skills (`SKILL.md`) & `n8n` Workflows

[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-io.github.truonggiang0111-10b981?style=flat-square)](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.truonggiang0111)
[![Apify Profile](https://img.shields.io/badge/Apify%20Store-ttyan0111-2563eb?style=flat-square)](https://apify.com/ttyan0111)
[![Agent Skills](https://img.shields.io/badge/skills.sh-Compatible-6366f1?style=flat-square)](#-install-portable-agent-skills-claude-code--cursor--codex)

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
| **Substack Creator Leads** *(rolling out)* | Direct creator emails, subscriber tiers, paid pricing plans & post engagement | Yes | `$0.006` + `$2.00/1k` pubs | [Skill Guide](./skills/substack-creator-leads/SKILL.md) |
| **Chrome Web Store Spy** *(rolling out)* | Developer support emails, install counts, ratings & negative review pain tags | Yes | `$0.006` + `$2.00/1k` ext | [Skill Guide](./skills/chrome-web-store-spy/SKILL.md) |

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

## 3. Ready-to-Import `n8n` Workflows

Import these JSON files directly into **n8n** and swap in your Apify token (`$5/month` free credit covers dozens of scheduled runs):

- [`workflows/n8n/weekly-competitor-app-bug-spy.n8n.json`](./workflows/n8n/weekly-competitor-app-bug-spy.n8n.json) — Weekly `1★–2★` competitor review & crash-bug digest across iOS & Android.
- [`workflows/n8n/daily-uk-au-direct-employer-leads.n8n.json`](./workflows/n8n/daily-uk-au-direct-employer-leads.n8n.json) — Daily UK (`Reed.co.uk`) + AU (`Seek.com.au`) direct-employer hiring leads merged into one pipeline.
- [`workflows/n8n/weekly-google-ads-winning-creatives.n8n.json`](./workflows/n8n/weekly-google-ads-winning-creatives.n8n.json) — Weekly tracker of competitor ads running `30+` days + EU DSA reach metrics.

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
