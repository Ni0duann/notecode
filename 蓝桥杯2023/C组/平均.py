n = int(input())
s = [[]for i in range(10)]
for i in range(n):
    a,b = map(int,input().split())
    s[a].append(b)
for i in range(10):
    s[i].sort()
res,c = 0 ,n //10
for i in range(10):
    if len(s[i]) > c:
        res += sum(s[i][:len(s[i]) - c])
print(res)
