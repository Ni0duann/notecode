arr = [2021] * 10
ans = 0
while True:
    for i in range(len(str(ans+1))):
        if arr[int(str(ans+1)[i])] <= 0:
            print(ans)
            exit()
        else:
            arr[int(str(ans+1)[i])] -= 1
    ans +=1

