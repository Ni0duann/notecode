N,K = map(int,input().split())
a = [int(i) for i in input().split()]
ans = 0
for i in range(N):
    count = 0
    for j in range(i,N-1):
        if a[j+1] >= a[j]:
            count += 1
        else:
            ans = max(count,ans)
print(ans)