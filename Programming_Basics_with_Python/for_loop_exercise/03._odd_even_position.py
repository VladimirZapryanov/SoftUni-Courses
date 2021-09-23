import sys
count_of_numbers = int(input())
sum_of_odd_numbers = 0
max_odd_number = -sys.maxsize
min_odd_number = sys.maxsize
sum_of_even_numbers = 0
max_even_numbers = -sys.maxsize
min_even_numbers = sys.maxsize
for position in range(1, count_of_numbers + 1):
    current_number = float(input())
    if position % 2 == 0:
        sum_of_even_numbers += current_number
        if current_number > max_even_numbers:
            max_even_numbers = current_number
        if current_number < min_even_numbers:
            min_even_numbers = current_number
    else:
        sum_of_odd_numbers += current_number
        if current_number > max_odd_number:
            max_odd_number = current_number
        if current_number < min_odd_number:
            min_odd_number = current_number
print(f"OddSum={sum_of_odd_numbers:.2f},")
if min_odd_number == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={min_odd_number:.2f},")
if max_odd_number == -sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={max_odd_number:.2f},")
print(f"EvenSum={sum_of_even_numbers:.2f},")
if min_even_numbers == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={min_even_numbers:.2f},")
if max_even_numbers == -sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={max_even_numbers:.2f}")