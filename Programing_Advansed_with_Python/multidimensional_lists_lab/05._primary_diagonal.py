square_size = int(input())

matrix = []

for _ in range(square_size):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

primary_diagonal = [matrix[x][x] for x in range(square_size)]

print(sum(primary_diagonal))
