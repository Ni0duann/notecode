a = 12345678
b = 98765432
s ="2023"
ans = 0
for i in range(a,b+1):
    c = str(i)
    pos = 0
    for j in range(len(c)):
        if c[j] == s[pos]:
            pos += 1
        if pos == 4:
            ans +=1
            break
print(b-a-ans+1)