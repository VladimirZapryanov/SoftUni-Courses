def read_matrix():
    rows, columns = [int(x) for x in input().split(", ")]
    matrix = []

    for _ in range(rows):
        numbers = [int(x) for x in input().split(", ")]
        matrix.append(numbers)
    return matrix


total_sum = 0

matrix = read_matrix()

for el in matrix:
    total_sum += sum(el)

print(total_sum)
print(matrix)