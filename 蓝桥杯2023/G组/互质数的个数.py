import math
a,b = map(int,input().split())
mod = 998244353
#快速幂
def qmi(m,k,p):
    res = 1 % p
    t = m 
    while k:
        if k&1:
            res = res * t % p
        t = t * t % p
        k >>= 1
    return res


#欧拉函数
def euler_phi(n):
    ans = n
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            ans = ans // i *(i-1)
            while n % i == 0:
                n = n // i
    if n > 1:
        ans = ans // n * (n-1)
    return ans

print(qmi(a,b-1,mod)*euler_phi(a) % mod)