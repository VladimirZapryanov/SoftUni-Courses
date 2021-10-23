def is_inside(r, c, length):
    if 0 <= r < length and 0 <= c < length:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    return r, c + 1


size = int(input())
matrix = [[0 for j in range(size)] for i in range(size)]
snake_row, snake_col = 0, 0
food_quantity = 0
is_won = True


for row in range(size):
    elements = input()
    for col in range(size):
        element = elements[col]
        if element == 'S':
            snake_row, snake_col = row, col
        matrix[row][col] = element

while food_quantity < 10:
    command = input()
    next_snake_row, next_snake_col = get_next_position(command, snake_row, snake_col)
    matrix[snake_row][snake_col] = '.'
    if is_inside(next_snake_row, next_snake_col, size):
        if matrix[next_snake_row][next_snake_col] == '*':
            food_quantity += 1
        elif matrix[next_snake_row][next_snake_col] == 'B':
            matrix[next_snake_row][next_snake_col] = '.'
            for row in range(size):
                for col in range(size):
                    if matrix[row][col] == 'B':
                        next_snake_row, next_snake_col = row, col
                        matrix[next_snake_row][next_snake_col] = 'S'
                        continue

        matrix[next_snake_row][next_snake_col] = 'S'
        snake_row, snake_col = next_snake_row, next_snake_col
    else:

        is_won = False
        break

if is_won:
    print(f"You won! You fed the snake.")
    print(f"Food eaten: {food_quantity}")
else:
    print(f"Game over!")
    print(f"Food eaten: {food_quantity}")
for i in matrix:
    print(''.join(str(x) for x in i))
