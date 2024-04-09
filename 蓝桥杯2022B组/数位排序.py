# n=int(input())
# m=int(input())
# d={}
# for i in range(1,n+1):
#     s=list(map(int,str(i)))
#     d[i]=sum(s)
# l=list(d.items())
# print(l)
# l.sort(key=lambda x:x[1])
# print(l)
# print(l[m-1][0])
n = int(input())
m = int(input())
d = {}
for i in range(1,n+1):
    s = list(map(int,str(i)))
    d[i]=sum(s)
l = list(d.items())
l.sort(key=lambda x:x[1])
print(l[m-1][0])