def gcd(a, b):
    return gcd(b, a % b) if b else a


d = [
    0, 0, 1, 2, 1, 4, 5, 4, 1, 2, 9, 0, 5, 10, 11, 14, 9, 0, 11, 18, 9, 11, 11,
    15, 17, 9, 23, 20, 25, 16, 29, 27, 25, 11, 17, 4, 29, 22, 37, 23, 9, 1, 11,
    11, 33, 29, 15, 5, 41, 46
]

# ans为结果，id为模数，lcm初值为2（即一开始的模数为2）

id = 2
while id <= 49:
  if id == 2:
      lcm, ans = id, d[id]
  if ans % id == d[id]:
      lcm = lcm // gcd(lcm, id) * id
      id += 1
  else:
      ans += lcm
print(ans)