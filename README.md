## BeaconReach v0.1: Open Source GTM Standard

**The Ethical, Asset-Based Outreach Protocol.**  
*Stop renting your pipeline. Own your graph.*

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

### 🛑 The Problem

Modern, proprietary GTM tools (like Clay, Apollo, etc.) are powerful, but they trap you in **Vendor Lock-in** and **Credit-Based Pricing**. You pay a markup on data, you don't own your workflows, and when you stop paying, your "brain" disappears.

### 💡 The BeaconReach Solution

BeaconReach is an open-source standard for **High-Personalization, Value-First Outreach**. It is not a SaaS. It is a framework.

1.  **Zero Credit Markup:** Use your own API keys (OpenAI, Perplexity, Google). Pay cost price.
2.  **Infrastructure-as-Code:** Version control your outreach strategies.
3.  **Ethical by Design:** Built on the "Value-First" protocol. No spam.
4.  **Dual-Mode:** Accessible for spreadsheets (Beginners) and Python/Pandas (Engineers).

---

### 🚀 Getting Started

#### Path A: The Human (Beginner / Manual)

*For founders, consultants, and those who want to keep it simple.*

👉 **[Read the Beginner Guide](guides/BEGINNER_START.md)**
1. Edit `data/contacts_master.csv` in Excel/Sheets.
2. Select a template from `templates/`.
3. Send manually, log the result.

#### Path B: The Engineer (Advanced / Automated)

*For Clay refugees, GTM Engineers, and Ops teams.*

👉 **[Read the Advanced Guide](guides/ADVANCED_GTM.md)**
1. Define your asset logic in `library/asset_manifest.json`.
2. Configure your API keys in `.env`.
3. Run the engine:
   ```bash
   python workflows/core_engine.py --enrich --generate
   ```

---

### 🧠 The Philosophy

We believe in the **Zen of Outreach** (see [BEACONREACH.md](BEACONREACH.md)).

> "Value is the only currency. If you aren't depositing, you can't withdraw."

**[BeaconReach.org](https://beaconreach.org)**

---

## License

This project is dedicated to the public domain under the **CC0 1.0 Universal** license.  
You are free to copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission.

While not required, we appreciate a link back to [BeaconReach.org](https://beaconreach.org) so others can find the standard.
