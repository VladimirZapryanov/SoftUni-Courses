numbers = int(input())

all_numbers_count = 0

for n in range(numbers):
    num = int(input())
    all_numbers_count += num

print(f'{all_numbers_count / numbers:.2f}')