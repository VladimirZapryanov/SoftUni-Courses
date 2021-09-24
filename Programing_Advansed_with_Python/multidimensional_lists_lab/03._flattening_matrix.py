rows = int(input())

matrix = []
flattening_matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

for row in matrix:
    flattening_matrix += row

print(flattening_matrix)