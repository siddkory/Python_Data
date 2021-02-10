from collections import Counter
from itertools import groupby
from functools import reduce
from operator import  iconcat

l = [1, 2, 1, 3, 42, 1, 1, 52, 3, 3, 4, 4, 2, 8, 2, 4, 6, 3, 5, 7, 2]
counter_dict = Counter(l)
group_obj = groupby(l)

print(counter_dict)
for i, g in group_obj:
    print(i, list(g))
