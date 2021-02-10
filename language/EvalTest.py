def calculator(num1, operator, num2):
    try:
        return eval("{0} {1} {2}".format(num1, operator, num2))
    except ZeroDivisionError as e:
        return "Can't divide by 0!"


print(calculator(1, "/", 0))
