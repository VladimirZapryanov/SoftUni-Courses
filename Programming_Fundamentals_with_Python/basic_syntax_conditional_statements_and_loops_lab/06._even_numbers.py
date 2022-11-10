numbers_count = int(input())

all_numbers_are_even = True
for _ in range(numbers_count):
    number = int(input())

    if number % 2 == 1:
        all_numbers_are_even = False
        print(f'{number} is odd!')
        break

if all_numbers_are_even:
    print('All numbers are even.')