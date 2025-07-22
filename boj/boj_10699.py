# print today's date in Seoul in YYYY-MM-DD format
from datetime import datetime, timedelta, timezone

seoul_tz = timezone(timedelta(hours=9))  # Seoul is UTC+9
today = datetime.now(seoul_tz)
print(today.strftime("%Y-%m-%d"))
