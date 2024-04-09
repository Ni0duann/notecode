n,len= map(int,input().split())
nums = []
for _ in range(n):
    nums.append([int(i) for i in input().split()])
nums.sort(key=lambda x:x[1])


def check(t):
    lines = []
    cnt = 0
    for pos , time in nums:
        if time > t:
            break
        lines.append([pos - (t-time),pos + (t - time)])
        cnt += 1
    #区间合并
    if not lines:
        return False
    lines.sort(key=lambda x:x[0])
    l , r = lines[0][0],lines[0][1]
    if l > 1:
        return False
    i = 0
    while r < len and i < cnt:
        if lines[i][0] > r + 1:
            break
        else:
            r = max(lines[i][1],r)
        i +=1
    return r >=len
l,r = 1,2e9
while l < r :
    mid = (l + r) // 2
    if check(mid) :
        r = mid 
    else :
        l = mid + 1
print(int(r))