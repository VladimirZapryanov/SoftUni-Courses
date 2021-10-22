def is_inside(r, c, board):
    if 0 <= r < board and 0 <= c < board:
        return True
    return False


size = int(input())

matrix = []

alice_row, alice_col = 0, 0
bags_of_tea = 0

enough_tea = True

for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "A":
            alice_row, alice_col = row, col

while True:
    direction = input()
    matrix[alice_row][alice_col] = "*"
    if direction == "right":
        alice_row, alice_col = alice_row, alice_col + 1
        if is_inside(alice_row, alice_col, size):
            symbol = matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = "*"
            if symbol.isdigit():
                bags_of_tea += int(symbol)
                if bags_of_tea >= 10:
                    break
            elif symbol == "R":
                enough_tea = False
                break
        else:
            enough_tea = False
            break

    elif direction == "left":
        alice_row, alice_col = alice_row, alice_col - 1
        if is_inside(alice_row, alice_col, size):
            symbol = matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = "*"
            if symbol.isdigit():
                bags_of_tea += int(symbol)
                if bags_of_tea >= 10:
                    break
            elif symbol == "R":
                enough_tea = False
                break
        else:
            enough_tea = False
            break

    elif direction == "up":
        alice_row, alice_col = alice_row - 1, alice_col
        if is_inside(alice_row, alice_col, size):
            symbol = matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = "*"
            if symbol.isdigit():
                bags_of_tea += int(symbol)
                if bags_of_tea >= 10:
                    break
            elif symbol == "R":
                enough_tea = False
                break
        else:
            enough_tea = False
            break

    elif direction == "down":
        alice_row, alice_col = alice_row + 1, alice_col
        if is_inside(alice_row, alice_col, size):
            symbol = matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = "*"
            if symbol.isdigit():
                bags_of_tea += int(symbol)
                if bags_of_tea >= 10:
                    break
            elif symbol == "R":
                enough_tea = False
                break
        else:
            enough_tea = False
            break

if enough_tea:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for el in matrix:
    print(" ".join(el))
