from itertools import groupby, product, combinations, permutations, accumulate

txt = "UUDDDDUUDDUUDDDDDDUUUU"
groupby_var = groupby(txt)
height = 0
valley_counter = 0
for k, g in groupby_var:
    lst_g = list(g)
    print(" k:", k, end='')
    print(", g:", lst_g)
    prev_height = height
    height = height + len(lst_g) if k == 'U' else height - len(lst_g)
    if prev_height >= 0 and height < 0:
        valley_counter += 1
print(valley_counter)

txt2 = "AABBCCCCFFDEEEEEKKCCDDJJJJJJJJZZZOOVVWXXXX YY ZZ"
groupby_var2 = groupby(txt2)
for k, g in groupby_var2:
    lst_g = tuple(g)
    print(" k:", k, end='')
    print(", g:", lst_g)

employees = [{"name": "sidd", "city": "denver", "age": 40},
             {"name": "raj", "city": "nyc", "age": 45},
             {"name": "sri", "city": "chicago", "age": 35},
             {"name": "john", "city": "sf", "age": 35}]

groupby_var3 = groupby(employees, key=lambda x: x["age"])
for k, g in groupby_var3:
    lst_g = tuple(g)
    print(" k:", k, end='')
    print(", g:", lst_g)


def group_txt_sorted_keyfunc(data):
    groups = []
    uniquekeys = []
    count = []
    keyfunc = lambda x: x.lower()  # doesn't make difference for ALL Uppper or lower case
    data = sorted(data, key=keyfunc)
    print('sorted data : ', ''.join(data))
    print('groupby data : ', dict(groupby(data, key=keyfunc)))
    for k, g in groupby(data, keyfunc):
        group = list(g)
        groups.append(group)  # Store group iterator as a list
        uniquekeys.append(k)
        count.append(len(group))
    return uniquekeys, groups, count


def group_txt(txt):
    keys = [key for key, group in groupby(txt)]
    groups = [list(group) for key, group in groupby(txt)]
    return keys, groups

print("-----------------group_txt--------------------------")

keys, groups = group_txt('AAAABBBCCDAABBB')
print(keys, groups)
print(''.join(keys), ''.join(i for lst in groups for i in lst))

print("------------------group_txt_sorted_keyfunc-----------------------------")
unique_keys, unique_groups, count = group_txt_sorted_keyfunc('AAAABBBCCDAABBB')
print(unique_keys, unique_groups)
print(''.join(unique_keys), ''.join(item for lst in unique_groups for item in lst), count)

print("-----------------------------------------------")

"""
Validing product 
"""
b = 10  # Spending amount. Get the max that you can buy
drives = [10, 3, 8]
keyboards = [3, 1]
com = product(drives, keyboards)

sum_ = sorted(list(map(lambda x: x[0] + x[1] , com)), reverse=True)

for i in sum_:
    if i < b:
        print(i)
