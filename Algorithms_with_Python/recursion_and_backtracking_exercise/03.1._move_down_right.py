def exit_count(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += exit_count(row, col + 1, rows, cols)
    result += exit_count(row + 1, col, rows, cols)

    return result


rows = int(input())
cols = int(input())

print(exit_count(0, 0, rows, cols))