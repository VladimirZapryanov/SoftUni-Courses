rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

biggest_sum = 0
best_col = 0
best_row = 0

for c in range(columns - 1):
    for r in range(rows - 1):
        value = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
        if value > biggest_sum:
            biggest_sum = value
            best_col = c
            best_row = r


print(matrix[best_row][best_col], matrix[best_row][best_col + 1])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1])
print(biggest_sum)
