n = int(input())
q = list(map(int,input().split()))
def quick_sort(q:list,l:int,r:int):
    if l >= r:
        return
    i = l - 1
    j = r + 1
    x = q[(l+r) // 2]
    while i < j:
        i +=1
        while q[i] < x:
            i += 1
        j -= 1
        while q[j] > x:
            j -= 1
        if i < j:
            q[i] , q[j] = q[j] ,q[i]
        quick_sort(q,l,j)
        quick_sort(q,j+1,r)
quick_sort(q,0,n-1)
for i in range(n):
    print(q[i],end=" ")
