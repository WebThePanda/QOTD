import requests
import os

# Get webhook URL from environment variable
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Fetch a random quote (using ZenQuotes API as example)
response = requests.get("https://zenquotes.io/api/random")
data = response.json()
quote = f"{data[0]['q']} — {data[0]['a']}"

# Send to Discord
requests.post(WEBHOOK_URL, json={"content": quote})