s=[0 for i in range(10**5+10)]
n=int(input())
f=list(map(int,input().split()))
for i in f:
    if i<10**5:
        s[i]+=1
for i in range(1,10**5+1):
    if s[i]%(i+1)!=0:
        print(i)
        exit()
    s[i+1]+=s[i]//(i+1)
print(min(f))