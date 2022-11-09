numbers_count = int(input())

numbers_division_on_two = 0
numbers_division_on_three = 0
numbers_division_on_four = 0
for _ in range(numbers_count):
    number = int(input())

    if number % 2 == 0:
        numbers_division_on_two += 1
    if number % 3 == 0:
        numbers_division_on_three += 1
    if number % 4 == 0:
        numbers_division_on_four += 1

percent_numbers_of_two = numbers_division_on_two / numbers_count * 100
percent_numbers_of_three = numbers_division_on_three / numbers_count * 100
percent_numbers_of_four = numbers_division_on_four / numbers_count * 100
print(f'{percent_numbers_of_two:.2f}%')
print(f'{percent_numbers_of_three:.2f}%')
print(f'{percent_numbers_of_four:.2f}%')


