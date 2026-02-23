import requests
import os
import datetime


WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("Webhook URL not found. Did you set DISCORD_WEBHOOK_URL as a GitHub secret?")



response = requests.get("https://zenquotes.io/api/random", timeout=10)
response.raise_for_status()
data = response.json()[0]


start = datetime.date(2025, 12, 7)
today = datetime.date.today()

day = (today - start).days + 1

quote = data["q"]
author = data["a"]


payload = {
    "username": "QOTD",
    "embeds": [
        {
            "title": f"Quote of the Day - Day {day}",
            "description": quote,
            "color": 13209599,
            "fields": [
                {"name": "Author", "value": f"{author}", "inline": True},
                {"name": "Today's Date", "value": today.strftime("%B %d, %Y"), "inline": True}
            ],
            "footer": {
                "text": "Powered by ZenQuotes API — Made by @webthepanda"
            }
        }
    ]
}

result = requests.post(WEBHOOK_URL, json=payload)

if result.status_code == 204:
    print("✅ Quote posted successfully!")
else:
    print(f"❌ Failed to post quote: {result.status_code} - {result.text}")