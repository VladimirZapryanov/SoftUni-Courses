numbers_of_location = int(input())

gold_from_every_location = 0

for location in range(1, numbers_of_location + 1):
    expected_daily_gold = float(input())
    numbers_of_days_for_this_location = int(input())
    for day in range(numbers_of_days_for_this_location):
        daily_gold = float(input())
        gold_from_every_location += daily_gold

    average_yield = gold_from_every_location / numbers_of_days_for_this_location

    if average_yield >= expected_daily_gold:
        print(f"Good job! Average gold per day: {average_yield:.2f}.")
    else:
        print(f"You need {expected_daily_gold - average_yield:.2f} gold.")

    gold_from_every_location = 0
