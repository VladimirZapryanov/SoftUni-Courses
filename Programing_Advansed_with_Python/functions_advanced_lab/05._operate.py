def operate(operator, *args):
    result = 0

    if len(args) < 1:
        return None
    elif operator == "+":
        for el in args:
            result += el
        return result
    elif operator == "-":
        result = args[0]
        for el in args[1:]:
            result -= el
        return result
    elif operator == "*":
        result = 1
        for el in args:
            result *= el
        return result
    elif operator == "/":
        result = args[0]
        for el in args[1:]:
            result /= el
        return result


'''
some test:
print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 3, 4, 5))
print(operate("/", 20, 5, 2))
print(operate("+"))
'''
