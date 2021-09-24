square_size = int(input())

matrix = []

for _ in range(square_size):
    characters = [input()]
    matrix.append(characters)

symbol = input()
current_index = 0
symbol_index = 0
found_symbol = False

for x in matrix:
    x = "".join(x)
    if symbol in x:
        x = [x]
        current_index = matrix.index(x)
        found_symbol = True
    else:
        continue
    for el in x:
        if symbol in el:
            symbol_index = el.index(symbol)
    break


if found_symbol:
    print(f"({current_index}, {symbol_index})")
else:
    print(f"{symbol} does not occur in the matrix")