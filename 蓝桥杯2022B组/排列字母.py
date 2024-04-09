a = 'WHERETHEREISAWILLTHEREISAWAY'
# 将字母大小写互换技巧
# 'a' ^ 32 = 'A'
# 'A' ^ 32 = 'a'
b = list(a)
b.sort()
ans = ''.join(b)
print(ans)