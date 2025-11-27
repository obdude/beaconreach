<div align="center">
  <img src="assets/beaconreach.svg" alt="BeaconReach Logo" width="200" height="auto" />
  <h1>BeaconReach</h1>
  <p>
    <strong>The Headless Enrichment & GTM Engine</strong>
  </p>
  
  <p>
    <a href="LICENSE">
      <img src="https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg" alt="License: CC0-1.0">
    </a>
    <a href="https://beaconreach.org">
      <img src="https://img.shields.io/badge/Website-beaconreach.org-blue.svg" alt="Website">
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Status-Active_Beta-success.svg" alt="Status">
    </a>
  </p>
</div>

<br />

### ⚡ Build enrichment waterfalls at cost price. 0% Markup. Unlimited Scale.

**BeaconReach** is the open infrastructure for GTM Engineering. It replaces expensive "Spreadsheet SaaS" credit models with a transparent, local-first automation layer.

---

### 🛑 The Problem: The "Credit Arbitrage"
Modern enrichment tools are powerful, but they operate on a **Credit Arbitrage** business model.
- You pay a **10x-50x markup** on data (reselling you standard API calls as "Credits").
- **Waterfall Logic** is expensive to run and locked inside a proprietary UI.
- **Scale Limits:** Browsers crash after 20k rows; you can't process your Total Addressable Market (TAM) in one go.

### 💡 The Solution: Headless GTM
BeaconReach decouples your logic from the data provider. It allows you to build sophisticated enrichment waterfalls locally.

1.  **Bring Your Own Keys (BYOK):** Connect directly to OpenAI, Perplexity, Google, Prospeo, or Clearbit. Pay the raw API cost. No middleman markup.
2.  **Enrichment Waterfalls:** Chain providers (e.g., *Check Apollo -> if null, check Hunter -> if null, predict with AI*) using simple config or Python.
3.  **Unlimited Scale:** Process 1M+ rows locally. No browser memory leaks. No "per-seat" pricing.
4.  **Infrastructure as Code:** Version control your outreach strategies. Treat your GTM pipeline like software, not a messy web of Zaps.

---

### Features

- **Smart Waterfalls:** Cascading enrichment logic to maximize coverage and minimize cost.
- **Local Data Sovereignty:** Your contact graph lives in local JSON/CSV.
- **Portable Logic:** Run the same engine on your laptop or a headless server.
- **Template Engine:** Modular message generation using standard logic (Jinja2/Liquid style).
- **Tool Agnostic:** Swap data providers in one line of config.

---

### 🆚 The Stack Comparison

| Feature | Spreadsheet-based SaaS | BeaconReach (Open Source) |
| :--- | :--- | :--- |
| **Enrichment Cost** | High Markup ("Credits") | **Cost Price** (Direct API) |
| **Scale Limit** | ~20k rows (Browser Crash) | **Unlimited** (Hardware Limit) |
| **Logic** | Locked in UI / "Click-Ops" | Version Controlled Config/Code |
| **Data Ownership** | Rented (Disappears on churn) | **100% Owned** (Local / Git) |

---

### 🚀 Getting Started

BeaconReach is designed for two types of workflows:

#### 1. The Config Path (Low-Code)
*For Operations and Growth leads.*
Define your enrichment waterfalls and messaging logic using simple **YAML/JSON Configurations** and standard spreadsheets. No complex Python scripting required—just define the rules and run the engine.
👉 **[Read the Config Guide](docs/beginner_guide.md)**

#### 2. The Engineer Path (Code)
*For GTM Engineers and Python Power Users.*
Import the `core_engine` to programmatically orchestrate complex data pipelines, custom scrapers, and dynamic graph management.
👉 **[Read the Advanced Docs](docs/advanced_guide.md)**

---

### 🧠 The Philosophy: High-Signal Engineering
We reject "Spray and Pray." We believe in precision at scale.
> *See [BEACONREACH.md](BEACONREACH.md) for the full protocol.*

1.  **Precision > Volume:** Use code to gather context so you can send fewer, better messages.
2.  **Schema over Chaos:** Relationships are data. Structure them properly (JSON) before flattening them for sending (CSV).
3.  **Automate the Process, Not the Human:** Use APIs to fetch data; use humans to verify empathy.

---

<div align="center">
  <sub>Managed by the <a href="https://beaconreach.org">BeaconReach Community</a>. Released under CC0.</sub>
</div>
