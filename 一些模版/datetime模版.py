import datetime
# 日期类
a = datetime.date(2024,1,2)
print(a)
print(a.weekday())
# 时间类
b = datetime.time(10,25,30)
print(type(b))
print(b)
# 日期时间
c= datetime.datetime(2024,1,2,10,25,30)
print(c)
delta = datetime.timedelta(hours=24)
g = a + delta
print(g)