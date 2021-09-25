square_size = int(input())

matrix = []
primary_sum = 0
secondary_sum = 0

for _ in range(square_size):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for r in range(square_size):
    primary_sum += matrix[r][r]
    secondary_sum += matrix[r][square_size - r - 1]

print(abs(primary_sum - secondary_sum))
