a = input()
b = list(a)
x = 1189
y = 841
for i in range(1,int(b[-1])+1):
    if x > y :
        x =x//2
    else:
        y = y//2
if x > y:
    print(x)
    print(y)
else:
    print(y)
    print(x)
