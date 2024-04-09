s = input()
n = len(s)
dp = [0] * (n+2)  # 创建dp数组，令 dp[i] 表示以第 i 个字符结尾的松散子序列中的最大价值
val = {chr(i+97): i+1 for i in range(26)}  # 创建一个字母:值的字典,便于获取字母的值

for i in range(n):
    dp[i+2] = max(dp[i+1],dp[i]+val[s[i]]) 
print(dp[-1])


#英雄带的模版
#真的好强，递推最强模版
#看了一大堆都不懂
#这个一下子明白了
