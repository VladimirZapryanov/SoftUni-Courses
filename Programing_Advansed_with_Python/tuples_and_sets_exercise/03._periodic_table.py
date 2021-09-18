numbers_of_row = int(input())

unique_elements = set()

for _ in range(numbers_of_row):
    elements = input().split()
    [unique_elements.add(el) for el in elements]

[print(el) for el in unique_elements]
