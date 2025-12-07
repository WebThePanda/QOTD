import requests
import os
import datetime

# Get webhook URL from environment variable
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("Webhook URL not found. Did you set DISCORD_WEBHOOK_URL as a GitHub secret?")

# Fetch a random quote (using ZenQuotes API)
try:
    response = requests.get("https://zenquotes.io/api/random", timeout=10)
    response.raise_for_status()
    data = response.json()
    quote = f"{data[0]['q']} — {data[0]['a']}"
except Exception as e:
    raise RuntimeError(f"Failed to fetch quote: {e}")

start = datetime.date(2025, 12, 7)
today = datetime.date(2025, 12, 8)

day = (today - start).days + 1

# Send to Discord
payload = {"content": f"# QOTD #{day}\n{quote}"}
result = requests.post(WEBHOOK_URL, json=payload)

if result.status_code == 204:
    print("✅ Quote posted successfully!")
else:
    print(f"❌ Failed to post quote: {result.status_code} - {result.text}")
