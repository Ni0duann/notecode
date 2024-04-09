N = int(input())
S = str(input())
a = list(str(S))
count_B = 0
count_E = 0
count_F = 1
for i in range(0,N-1) :
    if a[i] == 'F' :
        count_F *= 2
    