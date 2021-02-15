from collections import Counter, namedtuple, defaultdict, deque

# Counter
txt = "ilikeapple"
lst = list(txt)
print(lst)
counter = Counter(lst)
print("Counter : ", counter)
print("Counter by occurence : ", " p:", counter['p'], ", i:", counter['i'])
print("Counter tuples ordered by common ", counter.most_common())
print("Most Common Tuple : ", counter.most_common(1))
print("Most Common Value : ", counter.most_common(1)[0][0])

# NamedTuple acts like struct or data class with identifiers
Point = namedtuple("Point", "x,y")
p1 = Point(2, 3)
print("NameTuple p1.x : ", p1.x)
print("NameedTuple p1.y : ", p1.y)

# defaultDict. Takes type as constructor and assigns default value to unknown Key

intdict = defaultdict(int)
listdict = defaultdict(list)
strdict = defaultdict(str)

intdict["one"] = 1
intdict["two"] = 2
print('Default int :', intdict["three"])  # prints Zero
print('Default String :',strdict["test"])  # prints empty string
print('Default List :',listdict["test1"])  # prints empty list

#deque