from datetime import datetime, timezone, timedelta

file = open("time.txt", "w")
file.write(f'{datetime.now(timezone(timedelta(hours=+8))):%Y-%m-%d %H:%M}')
file.close()