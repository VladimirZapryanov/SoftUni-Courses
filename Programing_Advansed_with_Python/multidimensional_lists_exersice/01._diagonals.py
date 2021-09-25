square_size = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(square_size):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

for r in range(square_size):
    primary_diagonal.append(matrix[r][r])
    secondary_diagonal.append(matrix[r][square_size-r-1])


print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
