#国赛含2天数

import datetime
delta = datetime.timedelta(1) #时间差是一天
y1 = datetime.date(1900,1,1)
y2 = datetime.date(9999,12,31)
res = 0
#位数不打可以直接模拟每一天得出的结果
while y1 < y2:
    if "2" in str(y1.year) or "2" in str(y1.month) or "2" in str(y1.day):
        res +=1
    y1 += delta
res += 1
print(res)