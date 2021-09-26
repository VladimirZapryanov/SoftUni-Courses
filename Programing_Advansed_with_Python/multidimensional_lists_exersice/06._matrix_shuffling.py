def is_valid_index(r, c, rows, columns):
    if r < 0 or c < 0 or r >= rows or c >= columns:
        return False
    return True


rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    character = input().split()
    matrix.append(character)

commands = input()
while not commands == "END":
    commands = commands.split()
    if not commands[0] == "swap" or not len(commands) == 5 or not is_valid_index(int(commands[1]), int(commands[2]), rows, columns) or not \
            is_valid_index(int(commands[3]), int(commands[4]), rows, columns):
        print("Invalid input!")
    else:
        matrix[int(commands[1])][int(commands[2])], matrix[int(commands[3])][int(commands[4])] = matrix[int(commands[3])][int(commands[4])], matrix[int(commands[1])][int(commands[2])]
        for row in matrix:
            print(" ".join(row))

    commands = input()
