from collections import deque


def is_valid_index(r, c, rows, cols):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return False
    return True


square_size = int(input())

matrix = []
bomb_coordination = deque()
alive_cells = 0
sum_of_alive_cells = 0

for _ in range(square_size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()
for el in bombs:
    el.split(", ")
    bomb_coordination.append(el)

for _ in range(len(bomb_coordination)):
    bomb_value_coordination = bomb_coordination.popleft()
    row, col = [int(x) for x in bomb_value_coordination.split(",")]
    bomb_value = matrix[row][col]

    if bomb_value <= 0:
        continue

    if is_valid_index(row - 1, col, square_size, square_size) and matrix[row - 1][col] > 0:
        matrix[row - 1][col] -= bomb_value
    if is_valid_index(row + 1, col, square_size, square_size) and matrix[row + 1][col] > 0:
        matrix[row + 1][col] -= bomb_value
    if is_valid_index(row, col - 1, square_size, square_size) and matrix[row][col - 1] > 0:
        matrix[row][col - 1] -= bomb_value
    if is_valid_index(row, col + 1, square_size, square_size) and matrix[row][col + 1] > 0:
        matrix[row][col + 1] -= bomb_value
    if is_valid_index(row - 1, col - 1, square_size, square_size) and matrix[row - 1][col - 1] > 0:
        matrix[row - 1][col - 1] -= bomb_value
    if is_valid_index(row - 1, col + 1, square_size, square_size) and matrix[row - 1][col + 1] > 0:
        matrix[row - 1][col + 1] -= bomb_value
    if is_valid_index(row + 1, col - 1, square_size, square_size) and matrix[row + 1][col - 1] > 0:
        matrix[row + 1][col - 1] -= bomb_value
    if is_valid_index(row + 1, col + 1, square_size, square_size) and matrix[row + 1][col + 1] > 0:
        matrix[row + 1][col + 1] -= bomb_value

    matrix[row][col] = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            sum_of_alive_cells += el

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")

for row in matrix:
    print(' '.join([str(x) for x in row]))
