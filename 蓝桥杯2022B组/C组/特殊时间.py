def check(n):
    if n.count('1')==3 or n.count('2')==3:
        return True 
    return False
day=[]

for m in range(1,13):
    for d in range(31):
        s = "%02d%02d"%(m,d)

        s1 = sorted(s)
        if check(s):
            day.append(s1)
hour = []
for h in range(0,24):
    for m in range(0,60):
        s = "%02d%02d"%(h,m)
        s1 = sorted(s)
        if check(s):
            hour.append(s1)
    
cnt = 0
for j in day:
    for k in hour:
        if j == k:
            cnt+=1


print(cnt*4)