def calculates(op, n1, n2):
    if operator == "multiply":
        return n1 * n2
    elif operator == "divide":
        return n1 // n2
    elif operator == "add":
        return n1 + n2
    elif operator == "subtract":
        return n1 - n2


operator = input()
number_1 = int(input())
number_2 = int(input())
print(calculates(operator, number_1, number_2))


