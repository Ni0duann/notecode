import datetime 
def is_ava(y,m,d):
    try :
        w = datetime.date(y,m,d)
    except:
        return 
    if w not in output:
        output.append(w)



date = input().split("/")
for i,j in enumerate(date):
    date[i] = int(j)
output =  []
if date[0] >= 60:
    y = 19 * 100 + date[0]
else:
    y = 20 * 100 + date[0]

is_ava(y,date[1],date[2])

if date[2] >= 60:
    y = 19 * 100 + date[2]
else:
    y = 20 * 100 + date[2]


is_ava(y,date[0],date[1])
is_ava(y,date[1],date[0])

output.sort()
for i in output:
    print(i)