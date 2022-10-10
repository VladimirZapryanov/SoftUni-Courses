moves = int(input())

total_score = 0
invalid_numbers = 0
numbers_between_zero_and_nine = 0
numbers_between_ten_and_nineteen = 0
numbers_between_twenty_and_twenty_nine = 0
numbers_between_thirty_and_thirty_nine = 0
numbers_between_fourty_and_fifty = 0

for m in range(1, moves + 1):
    number = int(input())

    if number < 0 or number > 50:
        total_score /= 2
        invalid_numbers += 1
    elif number <= 9:
        total_score += number * 0.2
        numbers_between_zero_and_nine += 1
    elif number <= 19:
        total_score += number * 0.3
        numbers_between_ten_and_nineteen += 1
    elif number <= 29:
        total_score += number * 0.4
        numbers_between_twenty_and_twenty_nine += 1
    elif number <= 39:
        total_score += 50
        numbers_between_thirty_and_thirty_nine += 1
    elif number <= 50:
        total_score += 100
        numbers_between_fourty_and_fifty += 1

print(f"{total_score:.2f}")
print(f"From 0 to 9: {numbers_between_zero_and_nine / moves * 100:.2f}%")
print(f"From 10 to 19: {numbers_between_ten_and_nineteen / moves * 100:.2f}%")
print(f"From 20 to 29: {numbers_between_twenty_and_twenty_nine / moves * 100:.2f}%")
print(f"From 30 to 39: {numbers_between_thirty_and_thirty_nine / moves * 100:.2f}%")
print(f"From 40 to 50: {numbers_between_fourty_and_fifty / moves * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / moves * 100:.2f}%")
