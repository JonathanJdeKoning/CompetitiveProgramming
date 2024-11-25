import datetime
ans = 0
start = datetime.datetime(1901, 1, 1)
while True:
    start += datetime.timedelta(days=1)
    if start.weekday() == 6 and start.day==1: ans += 1
    if start.year == 2000 and start.month == 12 and start.day == 31: break

print(ans) 