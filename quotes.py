import requests
import os
import datetime
import random


WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("Webhook URL not found. Did you set DISCORD_WEBHOOK_URL as a GitHub secret?")


def quotePoster():
    response = requests.get("https://zenquotes.io/api/random", timeout=10)
    response.raise_for_status()
    data = response.json()[0]
    
    start = datetime.date(2026, 3, 17)
    today = datetime.date.today()

    day = (today - start).days + 1

    quote = data["q"]
    author = data["a"]


    payload = {
        "username": "Pandakrok",
        "embeds": [
            {
                "title": f"Random action of the day - Day {day}",
                "description": f"**Quote of the Day**\n{quote}",
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

def questionPoster():
    response = requests.get('https://boneitis.org/today', timeout=10)
    response.raise_for_status()
    data = response.json()

    start = datetime.date(2026, 3, 17)
    today = datetime.date.today()

    day = (today - start).days + 1

    question = data['question']

    payload = {
        "username": "Pandakrok",
        "embeds": [
            {
                "title": f"Random action of the day - Day {day}",
                "description": f"**Question of the Day**\n{question}",
                "color": 13209599,
                "fields": [
                    {"name": "Today's Date", "value": today.strftime("%B %d, %Y"), "inline": True}
                ],
                "footer": {
                    "text": "Powered by BoneItIs API — Made by @webthepanda"
                }
            }
        ]
    }
    result = requests.post(WEBHOOK_URL, json=payload)

    if result.status_code == 204:
        print("✅ Question posted successfully!")
    else:
        print(f"❌ Failed to post question: {result.status_code} - {result.text}")



todaysChoice = random.randint(1, 2)
print(todaysChoice)

if todaysChoice == 1:
    quotePoster()
else:
    questionPoster()