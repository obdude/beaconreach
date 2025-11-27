"""
BeaconReach Core Engine (v0.1)
The Open Source Alternative to Credit-Based Enrichment.
"""

import pandas as pd
import json
import os
from jinja2 import Template
from datetime import datetime

# --- CONFIGURATION ---
DATA_PATH = "data/contacts_master.csv"
OUTPUT_PATH = "data/contacts_enriched.json"
TEMPLATE_PATH = "templates/01_value_drop.md"
ASSET_MANIFEST = "library/asset_manifest.json"

def load_data():
    """Load contacts from CSV into a Pandas DataFrame."""
    print("Loading Contact Graph...")
    df = pd.read_csv(DATA_PATH)
    return df

def mock_enrichment(row):
    """
    PLACEHOLDER: In a real scenario, this connects to APIs 
    (Clearbit, Apollo, Perplexity, Google Search) to get data.
    """
    # Logic: If they are a 'Founder', they care about 'Growth'.
    if "Founder" in row['role']:
        return {"pain_point": "scaling revenue", "suggested_asset": "growth_guide.pdf"}
    else:
        return {"pain_point": "efficiency", "suggested_asset": "ops_checklist.pdf"}

def generate_message(row, enrichment_data):
    """Hydrate the Jinja2 template with contact + enriched data."""
    with open(TEMPLATE_PATH, 'r') as f:
        t = Template(f.read())
    
    return t.render(
        name=row['name'],
        company=row['company'],
        pain_point=enrichment_data['pain_point'],
        asset_link=f"https://beaconreach.org/assets/{enrichment_data['suggested_asset']}"
    )

def run_pipeline():
    df = load_data()
    
    results = []
    
    print(f"Processing {len(df)} contacts...")
    
    for index, row in df.iterrows():
        # 1. Enrich
        enrichment = mock_enrichment(row)
        
        # 2. Generate
        message_draft = generate_message(row, enrichment)
        
        # 3. Structure Output (JSON Graph)
        contact_record = {
            "id": row['id'],
            "profile": row.to_dict(),
            "enrichment": enrichment,
            "draft_message": message_draft,
            "status": "ready_to_send",
            "timestamp": datetime.now().isoformat()
        }
        results.append(contact_record)
        
    # 4. Save to Graph
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"✅ Pipeline Complete. Data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    run_pipeline()
