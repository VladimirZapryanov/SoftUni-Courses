rows, columns = [int(x) for x in input().split()]

matrix = []
max_sum = float('-inf')
best_start_row = 0
best_start_columns = 0

for _ in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for r in range(rows - 2):
    for c in range(columns - 2):
        value = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + \
                matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] + \
                matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        if max_sum < value:
            max_sum = value
            best_start_row = r
            best_start_columns = c

print(f"Sum = {max_sum}")
print(matrix[best_start_row][best_start_columns], matrix[best_start_row][best_start_columns + 1], matrix[best_start_row][best_start_columns + 2])
print(matrix[best_start_row + 1][best_start_columns], matrix[best_start_row + 1][best_start_columns + 1], matrix[best_start_row + 1][best_start_columns + 2])
print(matrix[best_start_row+ 2][best_start_columns], matrix[best_start_row + 2][best_start_columns + 1], matrix[best_start_row + 2][best_start_columns + 2])
