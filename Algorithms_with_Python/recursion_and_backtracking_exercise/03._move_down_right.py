def make_matrix(rows, cols):
    matrix = []
    for r in range(rows):
        row = []
        matrix.append(row)
        for c in range(cols):
            row.append(0)
    return matrix


def is_valid_index(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return False
    return True


def is_visited(row, col, matrix):
    if matrix[row][col] == 'v':
        return True
    return False


def is_exit(row, col, rows, cols):
    if row == rows - 1 and col == cols - 1:
        return True
    return False


def mark(row, col, matrix, symbol):
    matrix[row][col] = symbol


def move_down_right(row, col, matrix, rows, cols, count):
    if not is_valid_index(row, col, matrix) or is_visited(row, col, matrix):
        return
    if is_exit(row, col, rows, cols):
        count.append(1)
        return

    mark(row, col, matrix, 'v')

    move_down_right(row, col + 1, matrix, rows, cols, count)
    move_down_right(row + 1, col, matrix, rows, cols, count)

    mark(row, col, matrix, '0')

    return len(count)


rows = int(input())
cols = int(input())

matrix = make_matrix(rows, cols)
print(move_down_right(0, 0, matrix, rows, cols, []))

