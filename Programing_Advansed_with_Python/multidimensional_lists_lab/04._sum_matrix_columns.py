rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

sum_of_columns = [sum(x) for x in zip(*matrix)]

for el in sum_of_columns:
    print(el)
    