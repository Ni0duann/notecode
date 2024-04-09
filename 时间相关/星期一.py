import datetime
start = datetime.date(1901,1,1)
end = datetime.date(2000,12,31)
delta = datetime.timedelta(1)
ans = 0
while start <= end:
    if start.isoweekday() == 1:
        ans += 1
    start += delta

print(ans)