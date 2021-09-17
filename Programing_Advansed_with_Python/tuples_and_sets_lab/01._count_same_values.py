numbers = [float(el) for el in input().split()]

new_numbers = {}

for el in numbers:
    new_numbers[el] = numbers.count(el)

for key, value in new_numbers.items():
    print(f"{key:.1f} - {value} times")
