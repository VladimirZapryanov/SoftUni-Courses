number_of_location = int(input())
average_gold = 0

for locate in range(1, number_of_location + 1):
    average_gold_kg = float(input())
    days_digging = int(input())
    for days in range(1, days_digging + 1):
        daily_gold = float(input())
        average_gold += daily_gold / days_digging
    if average_gold >= average_gold_kg:
        print(f"Good job! Average gold per day: {average_gold_kg:.2f}.")
        needed_gold = average_gold_kg - average_gold
    else:
        print(f"You need {needed_gold:.2f} gold.")