year = 2000
month = 1
data_index = 1
week_index = 6
flags = []  
while (year != 2020) or (month != 10) or (data_index != 2):
    if week_index == 1 or data_index ==1:
        flags.append(2)
    else:
        flags.append(1)
    if month == 4 or month == 6 or month == 9 or month == 11:
        if not (data_index % 30):
            month += 1
        data_index = data_index % 30 + 1
    elif month == 2 :
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if not (data_index % 29):
                month += 1
            data_index = data_index % 29 + 1
        else:
            if not (data_index % 28):
                month += 1
            data_index =data_index % 28 + 1
    else:
        if month == 12:
            if not (data_index % 31):
                month =month % 12 + 1
                year += 1
        else:
            if not(data_index % 31):
                month += 1
        data_index = data_index % 31 + 1
    week_index = week_index % 7 + 1
print(sum(flags))