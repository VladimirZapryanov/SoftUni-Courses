days_numbers = int(input())
hours_numbers = int(input())

total_cost = 0
for d in range(1, days_numbers + 1):
    current_cost = 0
    for h in range(1, hours_numbers + 1):
        if d % 2 == 0 and h % 2 == 1:
            current_cost += 2.50
        elif d % 2 == 1 and h % 2 == 0:
            current_cost += 1.25
        else:
            current_cost += 1

    total_cost += current_cost
    print(f'Day: {d} - {current_cost:.2f} leva')

print(f'Total: {total_cost:.2f} leva')