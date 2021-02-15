# LEGB Local, Enclosing, Global and Builtins scope

x = 'global x'


def outer_func():
    # global x  use globalx variable . Output will be innerx , outer x, outer x
    x = 'outer x'

    def inner_func():
        x = 'inner x'
        print(x)  # Prints first

    inner_func()
    print (x)  # Prints second


outer_func()
print(x)  # prints third

print('--------------------------------------------------------')


def outer_func2():
    x = 'outer x'

    def inner_func2():
        nonlocal x
        x = 'inner x'
        print(x)  # Prints first

    inner_func2()
    print(x)  # Prints second


outer_func2()
print(x)  # prints third
