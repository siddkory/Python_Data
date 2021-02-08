# [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D

from itertools import groupby


def group_txt_sorted_keyfunc(data):
    groups = []
    uniquekeys = []
    count = []
    keyfunc = lambda x: x.lower()
    data = sorted(data, key=keyfunc)
    print('sorted data : ', ''.join(data))
    print('groupby data : ', dict(groupby(data, keyfunc)))
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


keys, groups = group_txt('AAAABBBCCDAABBB')
print(keys, groups)
print(''.join(keys), ''.join(i for lst in groups for i in lst))

print("-----------------------------------------------")
unique_keys, unique_groups, count = group_txt_sorted_keyfunc('AAAABBBCCDAABBB')
print(unique_keys, unique_groups)
print(''.join(unique_keys), ''.join(item for lst in unique_groups for item in lst), count)

print("-----------------------------------------------")
