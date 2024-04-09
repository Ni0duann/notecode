def gcd(a,b):
    if b == 0:
        return a
    else :
        return(b,a%b)
n = int(input())
a = [int(i) for i in input().split()]

