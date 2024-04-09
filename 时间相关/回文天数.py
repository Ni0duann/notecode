import datetime
m = input()
start = datetime.date.strptime(m,"%Y%m%d")
d = start.date()

delta = datetime.timedelta(1)
d += delta

p1 = True
p2 = True

while p1 or p2:
    s = str(d).replace("-","")

    if s == s[::-1]:
        if p1:
            print(s)
            p1 =False
        y2 = s[:2] * 2
        if s == y2 + y2[::-1]:
            print(s)
            p2 = False
    d += delta