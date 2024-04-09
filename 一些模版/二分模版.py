while l < r:
    mid = (l+r+1) // 2
    if check():
        l = mid 
    else:
        r = mid - 1

#查找右边界点
while l < r:
    mid = (l + r )//2
    if chek():
        l = mid + 1
    else:
        r = mid
#查找左边界点