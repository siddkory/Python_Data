"""
Flatten lists

"""


def flatten_reducer_lambda(lst):
    from functools import reduce
    return reduce(lambda x, y: x + y, lst)


def flatten_operator(lst):
    import operator
    import functools
    # similar to above lambda except that we're using operator
    return functools.reduce(operator.add, lst)


def flatten_recursive(list_of_lists):
    # first get the individual list and than indvidual item in those lists
    return [item for single_list in list_of_lists for item in single_list]


lofl = [[1, 2, 3], [4, 5], [6, 7], [8], [9, 10]]
print(flatten_operator(lofl))
print(flatten_reducer_lambda(lofl))
print(flatten_recursive(lofl))