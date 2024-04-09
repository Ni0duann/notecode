def compare(nums,win,fail1,fail2):
    acount = 0
    ans = 0
    not_want = []
    for i in range(n):
        total = nums[win][i] - nums[fail1][i] - nums[fail2][i]
        if total > 0:
            ans +=1
            acount +=total
        else:
            not_want.append(total)
    not_want.sort(reverse=True)
    for i in not_want:
        if acount + i <= 0:
            break
        else:
            acount +=i
            ans += 1
    if ans == 0:
        return -1
    else:
        return ans


n = int(input())
nums = []
for _ in range(3):
    nums.append([int(i) for i  in input().split()])
ans = max(
    compare(nums,0,1,2),
    compare(nums,1,0,2),
    compare(nums,2,1,0)

)
print(ans)