# 能过80实例
# 没判断是否相等

# def dfs(s,t,n):
#     ans = 0
#     for i in range(1,n-1):
#         if s[0] != t[0] or s[- 1] != t[- 1]: return -1
#         if s[i] == t[i]:continue
#         if s[i] != t[i] and (s[i-1] != t[i-1] or s[i+1] != t[i+1]):
#             return -1
#         elif s[i] != t[i] and (s[i-1] == t[i-1] and s[i+1] == t[i+1]):
#             ans += 1
#     return ans
# d = int(input())
# res = []
# for i in range(d):
#     t ,s= input(),input()
#     n = len(t)
#     res.append(int(dfs(s,t,n)))
# for i in res:
#     print(i)



import sys
input = lambda: sys.stdin.readline().strip() # 这个比input()更快





for _ in range(int(input())):
    t, s = list(input()), list(input()) # 转成列表才能改
    n, ans = len(s), 0 # 字符串长度 答案
    for i in range(n): # 遍历 s
        if s[i] != t[i]: # 发现有跟 t 不一样的字符
            if 0 < i < n - 1 and s[i - 1] == s[i + 1] == t[i]: # 可以改
                s[i] = t[i]
                ans += 1
            else: # 否则无解
                ans = -1
                break
    print(ans)