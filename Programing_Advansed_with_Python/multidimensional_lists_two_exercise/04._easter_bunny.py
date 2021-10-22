def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size


size = int(input())

matrix = []

bunny_row, bunny_col = 0, 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "B":
            bunny_row, bunny_col = row, col

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
}

max_eggs = float("-inf")
best_direction = ""
best_path = []

for directions, step in directions.items():
    eggs = 0
    current_row, current_col = bunny_row, bunny_col
    path = []

    while True:
        current_row, current_col = step(current_row, current_col)
        if not is_inside(current_row, current_col, size):
            break

        if matrix[current_row][current_col] == "X":
            break
        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])

    if eggs > max_eggs:
        max_eggs, best_direction, best_path = eggs, directions, path

print(best_direction)
for step in best_path:
    print(step)
print(max_eggs)



