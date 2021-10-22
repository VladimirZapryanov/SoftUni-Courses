def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == "up":
        return r - 1, c
    if direction == "down":
        return r + 1, c
    if direction == "left":
        return r, c - 1
    return r, c + 1


def get_houses_in_range(size, r, c):
    houses = []
    if not is_outside(r - 1, c, size):
        houses.append([r - 1, c])
    if not is_outside(r + 1, c, size):
        houses.append([r + 1, c])
    if not is_outside(r, c - 1, size):
        houses.append([r, c - 1])
    if not is_outside(r, c + 1, size):
        houses.append([r, c + 1])
    return houses


presents = int(input())
size = int(input())

matrix = []

santa_row, santa_col = 0, 0
initial_good_kinds_count = 0

for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "S":
            santa_row, santa_col = row, col
        elif element == "V":
            initial_good_kinds_count += 1

good_kids_count = initial_good_kinds_count

while True:
    line = input()
    if line == "Christmas morning":
        break
    next_santa_row, next_santa_col = get_next_position(line, santa_row, santa_col)
    if matrix[next_santa_row][next_santa_col] == "V":
        good_kids_count -= 1
        presents -= 1

    elif matrix[next_santa_row][next_santa_col] == "C":
        houses_in_range = get_houses_in_range(size, next_santa_row, next_santa_col)
        for row, col in houses_in_range:
            if matrix[row][col] == "X":
                presents -= 1
            if matrix[row][col] == "V":
                presents -= 1
                good_kids_count -= 1
            matrix[row][col] = "-"
            if presents == 0:
                break

    matrix[santa_row][santa_col] = "-"
    matrix[next_santa_row][next_santa_col] = "S"
    santa_row, santa_col = next_santa_row, next_santa_col

    if presents == 0:
        break

if presents == 0 and good_kids_count > 0:
    print("Santa ran out of presents!")
for x in matrix:
    print(' '.join(x))
if good_kids_count == 0:
    print(f"Good job, Santa! {initial_good_kinds_count} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_count} nice kid/s.")
