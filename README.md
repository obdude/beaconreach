<br/>
<div align="center">
  <!-- <img src="URL_TO_YOUR_LOGO.png" alt="Beaconreach Logo" width="150"> -->
  <h1 align="center">💡 Beaconreach</h1>
  <p align="center">
    <strong>The Open-Source Outbound Workflow Engine.</strong>
    <br />
    <em class="text-gray-500">Like Zapier or Clay - but open, transparent, and 100% yours.</em>
  </p>
</div>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3.9+-brightgreen.svg" alt="Python Version"></a>
  <a href="#"><img src="https://img.shields.io/badge/Framework-Streamlit-red.svg" alt="Streamlit"></a>
  <a href="https://github.com/obdude/beaconreach"><img src="https://img.shields.io/github/stars/obdude/beaconreach?style=social" alt="GitHub Stars"></a>
</p>

---

### 🚀 What is Beaconreach?

Beaconreach helps you **automate your outreach** - without the vendor lock-in, the hidden logic, or the monthly bills. It's a full-stack solution to the core problem of starting meaningful, value-first conversations.

If you can describe your outreach process in steps, you can build it with Beaconreach. Each step - sourcing leads, enriching data, or acting on it - is a simple, independent **module**. You stay in control, you own your data, and you decide exactly how your workflows run.

### ⚡ Why People Love It

*   **💯 Free & Open:** 100% open-source (MIT License). Use it, fork it, and host it anywhere you want.
*   **🧩 Modular:** Plug new APIs, scrapers, or actions in minutes. The engine is built to be extended.
*   **🔍 Transparent:** Every process is visible. No hidden logic. See exactly where your data comes from.
*   **⚡ Lightweight & Fast:** A simple local database ensures the app is fast and never fetches the same data twice.
*   **🔒 Yours Forever:** No subscriptions. No rate limits. You own the code and your data.

---

### 🧩 How It Works: The "Source → Enrich → Act" Flow

Beaconreach runs on a simple, powerful three-step workflow. You chain together modules to create your perfect outreach process.

<div align="center">
  <p>
    <strong>1️⃣ SOURCE</strong><br>
    <em>Choose where your leads come from.</em><br>
    (e.g., CSV Upload, API, CRM Connector)
  </p>
  <p>▼</p>
  <p>
    <strong>2️⃣ ENRICH</strong><br>
    <em>Add or clean data for each lead.</em><br>
    (e.g., Validate Emails, Find Socials, Scrape Info)
  </p>
  <p>▼</p>
  <p>
    <strong>3️⃣ ACT</strong><br>
    <em>Do something with the enriched data.</em><br>
    (e.g., Draft AI Message, Push to CRM, Export CSV)
  </p>
</div>

---

### 🛠️ Getting Started

With Docker, you can unleash the power of Beaconreach with a single command.

#### Prerequisites

*   Docker & Docker Compose ([Install Guide](https://docs.docker.com/get-docker/))

#### Installation & Launch

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/obdude/beaconreach.git
    cd beaconreach
    ```

2.  **Configure API Keys:**
    ```bash
    # Copy the example environment file
    cp .env.example .env
    ```
    Now, open the `.env` file and add any necessary API keys (e.g., for OpenAI, Hunter.io).

3.  **Launch the application:**
    ```bash
    docker-compose up
    ```

4.  **Open your browser** and navigate to `http://localhost:8501`. Welcome to Beaconreach.

---

### 🗺️ Roadmap

Beaconreach will always stay simple and modular, but it's growing fast.

*   **🎯 Core Engine:** Visual workflow builder, real-time logs, and reusable workflow templates.
*   **🔌 Integrations:** Connectors for HubSpot, Salesforce, Notion, and Google Sheets. AI-powered message writing and direct email sending (SMTP, SendGrid).
*   **🌱 Community:** A public **Module Hub** for sharing community-built connectors and workflow templates.

---

### 🤝 Join the Movement

Beaconreach isn’t just software - it’s a movement to make outreach **ethical, open, and personal again.**

*   **💡 Share an Idea:** Got a module idea? Post it using our [suggestion template](link-to-your-github-issue-template).
*   **👩‍💻 Build Something:** Want to code? Build a new Source, Enrich, or Act module. See our `CONTRIBUTING.md` guide.
*   **📢 Spread the Word:** Share Beaconreach with your peers. Every mention grows the open outreach movement.

---

### ⚖️ Use It Ethically

Beaconreach is a powerful engine. **Use it responsibly.** It’s built for genuine, value-first conversations - **not for spam.** Respect privacy, consent, and all data laws (GDPR, CCPA, etc.). Let’s make outreach better, together.
