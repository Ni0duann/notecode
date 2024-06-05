#递推公式：dfs[i] = max(dfs[i-2]+1,dfs[i-1])
#前提是符合条件的时候
#否则dp[i] = dp[i-1]
s = input()
n = len(s)
dp = [0]*(n+1)
index = 0
for i in range(1,n):
    if s[i] == s[i-1] or s[i-1] == '?' or s[i] == '?':
        dp[index + 2] = max(dp[index] + 1,dp[index+1])
    else: 
        dp[index + 2] = dp[index+1]
    index += 1
print(dp[-1])

# import sys
# input = lambda: sys.stdin.readline().strip()