import sys

numbers_of_couples = int(input())
num1 = int(input())
num2 = int(input())

first_result = num1 + num2
max_difference = -sys.maxsize
is_equal = True

for n in range(2, numbers_of_couples + 1):
    num3 = int(input())
    num4 = int(input())
    current_result = num3 + num4

    if first_result != current_result:
        is_equal = False
        difference = abs(first_result - current_result)
        first_result = current_result
        if difference > max_difference:
            max_difference = difference

if not is_equal:
    print(f'No, maxdiff={max_difference}')
else:
    print(f'Yes, value={first_result}')