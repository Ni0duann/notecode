import math
n = 2021041820210418 
l = []  # ！！！！用于存因数不是因子例如：10=2*5
i = 2
x = n
while i < math.isqrt(x):
    if x % i == 0:
        l.append(i)
        x = x // i
    else:
        i += 1  # else才加1是要除尽
l.append(x)
s = set()  # ！！！！用于存因子 如10=1*2*5*10
s.add(1)
# print(s)
for j in l:
    p = set()
    for k in s:
        p.add(j * k)
    for k in p:
        s.add(k)
count = 0
for k1 in s:  # 遍历两层求解
    for k2 in s:
        if n % (k1 * k2) == 0:
            count += 1
print(count)
