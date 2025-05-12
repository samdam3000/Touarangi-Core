# Touarangi: The Core External Engine
# Role: Interface between live odds, match state, and Touarangi system modules

import time
import requests
from datetime import datetime

# CONFIGURATION
MATCH_SOURCES = {
    "NRL": "https://www.foxsports.com.au/nrl/nrl-premiership/match-centre",
    "NRLW": "https://www.foxsports.com.au/nrl/nrlw-premiership/match-centre",
    "ORIGIN": "https://www.foxsports.com.au/nrl/state-of-origin"
}

BET365_ENDPOINT = "https://api.bet365.com/feeds/odds"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL_HERE"

# CORE STATE
state = {
    "matches": [],
    "last_sync": None,
    "alerts": []
}

def fetch_match_data():
    try:
        response = requests.get(MATCH_SOURCES["NRL"])
        if response.status_code == 200:
            state["matches"] = response.text[:500]  # mock processing
            state["last_sync"] = datetime.utcnow().isoformat()
    except Exception as e:
        print("Error fetching data:", e)

def post_to_discord(message):
    try:
        data = {"content": message}
        requests.post(DISCORD_WEBHOOK, json=data)
    except Exception as e:
        print("Discord webhook failed:", e)

# EXAMPLE COMMAND FLOW
if __name__ == "__main__":
    fetch_match_data()
    post_to_discord(f"Arawhata synced at {state['last_sync']}")
