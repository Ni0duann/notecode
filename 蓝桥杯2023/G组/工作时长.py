import datetime
arr = []
ans = 0
n = 520
for i in range(n):
    x = input()
    imtem = datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S")
    arr.append(imtem)
arr.sort()
for i in range(1,n,2):
    ans += (arr[i]-arr[i-1]).seconds
print(ans)