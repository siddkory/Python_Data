a = (2, 3, 4)
b = (4, 3, 1)


def compare(x):
    a1, b1 = x
    if a1 > b1:
        return 1
    elif a1 < b1:
        return -1
    else:
        return 0


result = map(compare, zip(a, b))
a_val, b_val = 0, 0
for i in result:
    print(i)
    if i > 0:
        a_val += 1
    elif i < 0:
        b_val += 1
print(a_val, b_val)

