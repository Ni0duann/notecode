import datetime
a,b = int(input()) , int(input())
d = datetime.datetime(2024,3,31,a,b,0)
delta = datetime.timedelta(minutes=int(input()))
w = d + delta

print(w.hour)
print(w.minute)
