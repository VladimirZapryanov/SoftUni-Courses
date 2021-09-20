parenthesis = input()

parenthesis_stack = []
balanced = True

for el in parenthesis:
    if el in "({[":
        parenthesis_stack.append(el)
    else:
        if len(parenthesis_stack) == 0:
            balanced = False
            break
        last_opening_bracket = parenthesis_stack.pop()
        pair = f"{last_opening_bracket}{el}"
        if pair not in "(){}[]":
            balanced = False
            break

if len(parenthesis_stack) > 0:
    balanced = False

if balanced:
    print("YES")
else:
    print("NO")