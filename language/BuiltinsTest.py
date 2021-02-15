"""
https://docs.python.org/3/library/functions.html#ascii

built-in map is higher order function takes first arguments as func and than lists or tuples

"""
"""
Following functions returns some sort of Number
bin, hex, oct, int, float, divmod, pow, abs, round , complex, hash, id, max, min, range, sum
"""

"""
returns truth values
all(iterable), any(iterable),  bool(), isinstance, issubclass,
"""

"""
working with lists/iterables/sequences
enumerate, next, sorted, reversed, slice, iter, sum
immutables => frozenset, tuples, bytes, str  
mutables   => bytearray, list, set, dict, zip

"""

"""
Higher order functions
map, filter
"""
"""
Working with attributes
hasattr, setattr, getattr, deleteattr, dir
"""

"""
scope symbol tables
locals, globals
"""

"""
method decorators and class,objects
staticmethod, classmethod, super , isinstance, issubclass
"""

"""
language and runtime
.eval, exec, compile
"""

"""
ord and chr. Converts character to ascii number and viceversa
"""

"""
debug
help, input, .print
"""

func_seperator = '\n_______________________________________________________________________________'
seperator = '\n------------------------------------'
assert (list(map(lambda x: x ** 2, range(10))) == [x ** 2 for x in range(10)]), "Both are Equal !!!!! "
print(' Showing zip tuples : ', end='')
for x in zip(range(10), range(10)):
    print(x, ' ', end='')
print(seperator)

# Add two list number by passing individual numbers
add_two_lists = map(lambda x, y: x + y, list(range(10)), list(range(10)))
print(' Adding two plain lists : ', end='')
for i in add_two_lists:
    print(i, ' ', end='')
print(seperator)

# zip gives a 2 number tuple
add_two_zip_lists = map(lambda x: x[0] + x[1], zip(range(10), range(10)))
print(' Adding 2 zip lists : ', end='')
for i in add_two_zip_lists:
    print(i, ' ', end='')
print(seperator)

# zip gives a 3 number tuple
add_three_zip_lists = map(lambda x: x[0] + x[1] + x[2], zip(range(10), range(10), range(10)))
print(' Adding 3 lists  : ', end='')
for i in add_three_zip_lists:
    print(i, ' ', end='')
print(seperator)
print(func_seperator)

"""
builtin filter. It's a higher order function takes perdicate function as first parameter to filter list
"""
even_numbers = filter(lambda x: x % 2 == 0, range(10))
print('Even Numbers : ', end='')
for i in even_numbers:
    print(i, ' ', end='')
print(seperator)

# Filter takes only one argument. So values are variables like y should be assigned before
y = 50
above_number_50 = filter(lambda x: x > y, range(100))
print(list(above_number_50))

"""
ord and chr. Converts character to ascii number and viceversa
"""
ascii_number = ord('a')
char = chr(ascii_number)
print(" number , char : ", ascii_number, ', ', char)

print(list(globals()))
