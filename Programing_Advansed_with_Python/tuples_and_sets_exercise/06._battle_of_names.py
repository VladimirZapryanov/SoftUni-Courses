numbers_of_row = int(input())

odd_numbers = set()
even_numbers = set()
result = set()

for row in range(1, numbers_of_row + 1):
    name = input()
    name_value = sum([ord(el) for el in name]) // row
    if name_value % 2 == 0:
        even_numbers.add(name_value)
    else:
        odd_numbers.add(name_value)

if sum(odd_numbers) == sum(even_numbers):
    current_result = odd_numbers.union(even_numbers)
    [result.add(el) for el in current_result]
elif sum(odd_numbers) > sum(even_numbers):
    current_result = odd_numbers.difference(even_numbers)
    [result.add(el) for el in current_result]
elif sum(even_numbers) > sum(odd_numbers):
    current_result = odd_numbers.symmetric_difference(even_numbers)
    [result.add(el) for el in current_result]

print(f"{', '.join([str(el) for el in result])}")
