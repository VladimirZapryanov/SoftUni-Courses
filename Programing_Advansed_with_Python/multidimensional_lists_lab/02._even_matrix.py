rows = int(input())

result_matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    even_matrix = [x for x in numbers if x % 2 == 0]
    result_matrix.append(even_matrix)

print(result_matrix)