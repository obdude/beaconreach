<div align="center">
  <img src="assets/beaconreach.svg" alt="BeaconReach Logo" width="200" height="auto" />
  <h1>BeaconReach</h1>
  <p>
    <strong>The Open Protocol for GTM Engineering</strong>
    <br />
    <strong><i>GTM-as-Code</i></strong>
  </p>
  
  <p>
    <a href="LICENSE">
      <img src="https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg" alt="License: CC0-1.0">
    </a>
    <a href="https://beaconreach.org">
      <img src="https://img.shields.io/badge/Website-beaconreach.org-blue.svg" alt="Website">
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Registry-Available-success.svg" alt="Registry">
    </a>
  </p>
</div>

<br />

### ⚡ The Terraform for Growth. 0% Markup. Unlimited Scale.

**BeaconReach** is the standard definition language for Growth. It replaces expensive "Spreadsheet SaaS" credit models with a transparent, local-first automation protocol. 

It allows you to treat your Go-To-Market strategy like software: **Version controlled, testable, and priced at wholesale cost.**

---

### 🛑 The Problem: "Credit Arbitrage" & Logic Lock-in
Modern enrichment tools are powerful, but they are built on two flawed models:

1.  **Credit Arbitrage:** You pay a **10x-50x markup** on data. Vendors resell you standard API calls (OpenAI, Apollo, Google) disguised as "Credits."
2.  **Logic Lock-in:** Your complex waterfall logic is trapped inside a proprietary SaaS UI. You cannot version control it, you cannot diff it, and if you stop paying, you lose your intellectual property.
3.  **The Browser Ceiling:** SaaS tools crash after ~20k rows. You cannot process your Total Addressable Market (TAM) in one go without breaking the browser.

### 💡 The Solution: The BeaconReach Protocol
BeaconReach decouples your **Logic** from the **Vendor**.

1.  **Define in YAML:** Write your enrichment logic in a declarative `pipeline.yaml` file. "GTM-as-Code."
2.  **Bring Your Own Keys (BYOK):** Connect directly to Apollo, OpenAI, Perplexity, or any HTTP endpoint. **Pay the raw API cost ($0.002) not the Credit cost ($0.50).**
3.  **Unlimited Scale:** The engine runs on your metal (Laptop, Docker, Server). Process 1M+ rows without memory leaks.
4.  **The Registry:** Don't build from scratch. Pull community-verified waterfall strategies (e.g., `beaconreach pull community/local-business-scraper`) and run them instantly.

---

### 🛠️ The Standard: `pipeline.yaml`
BeaconReach uses a standardized syntax to define "Smart Waterfalls." If one provider fails, the engine intelligently falls back to the next, saving you money on every row.

```yaml
# pipeline.yaml
name: "Enterprise Founders Outreach v2"
version: "1.0.0"

input: 
  source: "data/raw_domains.csv"

# The Registry allows you to pull community-verified logic
# import: "beaconreach/waterfalls/b2b-founder-enrichment@latest"

waterfall:
  - field: "work_email"
    strategies:
      # 1. Precise API Call (Cost: ~$0.01)
      - provider: "apollo_api"
        api_key: ${APOLLO_KEY}
        params:
          reveal_personal_emails: false
        
      # 2. Fallback Scrape (Cost: ~$0.005)
      - provider: "prospeo_api"
        condition: "if_previous_failed"
        
      # 3. AI Inference (Cost: ~$0.03)
      # Only runs if previous steps failed. Prevents waste.
      - provider: "openai_reasoning"
        model: "gpt-4o"
        prompt: "templates/email_guesser.j2"
        condition: "if_previous_failed"
        validation: "verify_smtp" 

output:
  format: "csv"
  path: "data/ready_to_send.csv"
```

---

### 📦 The Toolkit

BeaconReach is designed for the **GTM Engineer**—the new breed of growth marketer who demands precision and control.

#### 1. The Pre-Flight Estimator
Never guess your spend. The CLI analyzes your pipeline and calculates the exact API cost before execution.

```bash
beaconreach estimate --input 5000_rows.csv
> Estimated Run Cost: $14.20
> SaaS Equivalent Cost: $450.00
> Potential Savings: 96%
```

#### 2. The Registry
Access the open-source library of enrichment strategies.
👉 **[Browse the Registry](docs/registry.md)**

#### 3. The Engine (Python SDK)
Import the core engine into your own Python scripts or FastAPI backends to build custom internal tools.
👉 **[SDK Documentation](docs/sdk_guide.md)**

---

### 🆚 Philosophy: App vs. Protocol

| Feature | The "App" Model (Clay, Spreadsheets) | The "Protocol" Model (BeaconReach) |
| :--- | :--- | :--- |
| **Enrichment Cost** | High Markup ("Credits") | **Cost Price** (Direct Wholesale API) |
| **Logic Storage** | Trapped in SaaS Database | **Git / Version Control** |
| **Scale Limit** | ~20k rows (Browser Crash) | **Unlimited** (Hardware Limit) |
| **Collaboration** | Share Workspace Login | **Pull Requests & Code Review** |
| **Extensibility** | Wait for Vendor Integration | **Generic HTTP / Python Scripting** |

---

### 🧠 The Philosophy: High-Signal Engineering
We reject "Spray and Pray." We believe in precision at scale.

1.  **Precision > Volume:** Use code to gather context so you can send fewer, better messages.
2.  **Schema over Chaos:** Relationships are data. Structure them properly (JSON) before flattening them for sending (CSV).
3.  **Automate the Process, Not the Human:** Use APIs to fetch data; use humans to verify empathy.

---

<div align="center">
  <sub>Managed by the <a href="https://beaconreach.org">BeaconReach Community</a>. Released under CC0.</sub>
</div>
