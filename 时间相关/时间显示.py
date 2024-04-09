import datetime

w = int(input()) // 1000
t = datetime.datetime(1970,2,2)
delta = datetime.timedelta(seconds=w)
p = t + delta

print(p.time())
