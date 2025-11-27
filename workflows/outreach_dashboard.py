"""
BeaconReach Outreach Dashboard (v0.1)
A Clear, Human-Friendly KPI Report for ABM Campaigns.
"""

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from jinja2 import Template


# -------------------------------------------------
# CONFIGURATION
# -------------------------------------------------
ENRICHED_DATA = "data/contacts_enriched.json"
HTML_OUTPUT = "reports/outreach_dashboard.html"
CHARTS_DIR = "reports/charts"

os.makedirs("reports", exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)


# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
def load_enriched_contacts():
    """Load contact graph from core_engine export."""
    if not os.path.exists(ENRICHED_DATA):
        raise FileNotFoundError(
            f"❌ Missing enriched contacts file: {ENRICHED_DATA}\n"
            f"Run `core_engine.py` first."
        )
    
    with open(ENRICHED_DATA, "r") as f:
        data = json.load(f)
    
    df = pd.json_normalize(data)
    return df


# -------------------------------------------------
# KPI CALCULATIONS
# -------------------------------------------------
def calculate_kpis(df):
    """Return a dict with outreach KPIs."""
    now = datetime.now()

    # Count assets per contact (from suggested_asset)
    df["asset"] = df["enrichment.suggested_asset"]

    # Days since generated (used as "freshness")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["days_since_generated"] = (now - df["timestamp"]).dt.days

    return {
        "total_contacts": len(df),
        "ready_to_send": (df["status"] == "ready_to_send").sum(),
        "unique_assets": df["asset"].nunique(),
        "avg_days_since_generated": round(df["days_since_generated"].mean(), 2),
        "top_pain_points": df["enrichment.pain_point"].value_counts().to_dict(),
    }


# -------------------------------------------------
# CHART GENERATION
# -------------------------------------------------
def generate_charts(df):
    """Create simple charts saved to PNG files."""
    chart_files = {}

    # ---- Contacts by Pain Point ----
    plt.figure()
    df["enrichment.pain_point"].value_counts().plot(kind="bar")
    plt.title("Contacts by Pain Point")
    plt.xlabel("Pain Point")
    plt.ylabel("Count")
    pain_chart = f"{CHARTS_DIR}/pain_points.png"
    plt.savefig(pain_chart, bbox_inches="tight")
    plt.close()
    chart_files["pain_points"] = pain_chart

    # ---- Days Since Generated Histogram ----
    plt.figure()
    df["days_since_generated"].plot(kind="hist", bins=10)
    plt.title("Freshness of Outreach (Days Since Generated)")
    plt.xlabel("Days")
    days_chart = f"{CHARTS_DIR}/freshness.png"
    plt.savefig(days_chart, bbox_inches="tight")
    plt.close()
    chart_files["freshness"] = days_chart

    # ---- Assets Used ----
    plt.figure()
    df["asset"].value_counts().plot(kind="bar")
    plt.title("Asset Usage Distribution")
    plt.xlabel("Asset")
    plt.ylabel("Count")
    assets_chart = f"{CHARTS_DIR}/assets.png"
    plt.savefig(assets_chart, bbox_inches="tight")
    plt.close()
    chart_files["assets"] = assets_chart

    return chart_files


# -------------------------------------------------
# HTML REPORT
# -------------------------------------------------
def build_html_report(kpis, charts):
    """Render HTML using a Jinja-style mini-template."""
    template = Template("""
    <html>
    <head>
        <title>BeaconReach Outreach Dashboard</title>
        <style>
            body { font-family: Arial; padding: 20px; max-width: 850px; margin: auto; }
            h1 { color: #333; }
            .kpi-box { background: #f5f5f5; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
            img { max-width: 100%; margin-bottom: 30px; border-radius: 6px; }
            .chart-title { font-weight: bold; margin-top: 40px; }
        </style>
    </head>
    <body>

        <h1>📊 BeaconReach Outreach Dashboard</h1>
        <p>Generated at {{ timestamp }}</p>

        <div class="kpi-box">
            <h2>Key Metrics</h2>
            <p><strong>Total Contacts:</strong> {{ k.total_contacts }}</p>
            <p><strong>Ready to Send:</strong> {{ k.ready_to_send }}</p>
            <p><strong>Unique Assets Used:</strong> {{ k.unique_assets }}</p>
            <p><strong>Avg Days Since Generated:</strong> {{ k.avg_days_since_generated }}</p>
        </div>

        <h2>Pain Points Frequency</h2>
        <img src="{{ charts.pain_points }}" />

        <h2>Freshness (Days Since Generated)</h2>
        <img src="{{ charts.freshness }}" />

        <h2>Asset Usage</h2>
        <img src="{{ charts.assets }}" />

    </body>
    </html>
    """)

    html = template.render(
        k=kpis,
        charts=charts,
        timestamp=datetime.now().isoformat()
    )

    with open(HTML_OUTPUT, "w") as f:
        f.write(html)

    return HTML_OUTPUT


# -------------------------------------------------
# MAIN PIPELINE
# -------------------------------------------------
def run_dashboard():
    print("Loading enriched contact graph...")
    df = load_enriched_contacts()

    print("Calculating KPIs...")
    kpis = calculate_kpis(df)

    print("Generating charts...")
    charts = generate_charts(df)

    print("Rendering HTML dashboard...")
    output = build_html_report(kpis, charts)

    print(f"✅ Dashboard ready: {output}")


if __name__ == "__main__":
    run_dashboard()
