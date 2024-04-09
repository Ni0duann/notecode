n = int(input())
q = list(map(int,input().split()))
def merge_sort(q:list,l:int,r:int):
    if l >= r:
        return 
    mid = (l+r) // 2
    merge_sort(q,l,mid)
    merge_sort(q,mid+1,r)
    k = 0 
    i = 1
    j = mid + 1
    while i <= mid and j <= r:
        if q[i] <= q[j] :
            




# void merge_sort(int q[], int l, int r)
# {
#     if (l >= r) return;

#     int mid = l + r >> 1;
#     merge_sort(q, l, mid);
#     merge_sort(q, mid + 1, r);

#     int k = 0, i = l, j = mid + 1;
#     while (i <= mid && j <= r)
#         if (q[i] <= q[j]) tmp[k ++ ] = q[i ++ ];
#         else tmp[k ++ ] = q[j ++ ];

#     while (i <= mid) tmp[k ++ ] = q[i ++ ];
#     while (j <= r) tmp[k ++ ] = q[j ++ ];

#     for (i = l, j = 0; i <= r; i ++, j ++ ) q[i] = tmp[j];

# 作者：yxc
# 链接：https://www.acwing.com/blog/content/277/
# 来源：AcWing
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。