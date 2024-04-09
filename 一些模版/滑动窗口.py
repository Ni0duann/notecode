left,right = 0,0
windows_count = 0
while right < len(nums):
    windows_count += nums[right]
    if right - left + 1 >= len(windows):
        ans = max(ans,windows_count)
        windows_count -= nums[left]
        left += 1
    right += 1
return ans  