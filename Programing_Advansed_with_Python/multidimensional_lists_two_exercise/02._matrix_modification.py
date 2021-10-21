def is_valid_index(r, c, rows, columns):
    if r < 0 or c < 0 or r >= rows or c >= columns:
        return False
    return True


matrix_row = int(input())
matrix = []

for _ in range(matrix_row):
    character = [int(x) for x in input().split()]
    matrix.append(character)

commands = input()
while not commands == "END":
    data = commands.split()
    command = data[0]
    row = int(data[1])
    col = int(data[2])
    number = int(data[3])
    if command == "Add":
        if not is_valid_index(row, col, matrix_row, matrix_row):
            print("Invalid coordinates")
        else:
            matrix[row][col] += number
    elif command == "Subtract":
        if not is_valid_index(row, col, matrix_row, matrix_row):
            print("Invalid coordinates")
        else:
            matrix[row][col] -= number
    commands = input()

for el in matrix:
    print(" ".join(map(str, el)))
