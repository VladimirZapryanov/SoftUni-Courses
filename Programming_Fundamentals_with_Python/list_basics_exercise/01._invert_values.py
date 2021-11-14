numbers_str = input().split()

numbers_inversed = []

for number in numbers_str:
    number_inverted = int(number) * -1
    numbers_inversed.append(number_inverted)

print(numbers_inversed)