import datetime

start = datetime.date(2025, 12, 7)
today = datetime.date.today()

day = (today - start).days + 1

print(day)