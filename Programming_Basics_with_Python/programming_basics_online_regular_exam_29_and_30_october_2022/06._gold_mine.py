locations_number = int(input())

for _ in range(locations_number):
    average_yield_per_day = float(input())
    days_in_location = int(input())
    gold_yield_in_location = 0

    for _ in range(days_in_location):
        gold_yield_per_day = float(input())
        gold_yield_in_location += gold_yield_per_day

    average_yield_in_location = gold_yield_in_location / days_in_location
    if average_yield_per_day <= average_yield_in_location:
        print(f'Good job! Average gold per day: {average_yield_in_location:.2f}.')
    else:
        yield_difference = average_yield_per_day - average_yield_in_location
        print(f'You need {yield_difference:.2f} gold.')
