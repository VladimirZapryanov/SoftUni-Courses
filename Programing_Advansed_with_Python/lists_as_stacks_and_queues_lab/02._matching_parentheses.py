algebraic_expression = input()

ss = []

for index, character in enumerate(algebraic_expression):

    if character == "(":
        ss.append(index)
    elif character == ")":
        print(f"{algebraic_expression[ss.pop():index + 1]}")
