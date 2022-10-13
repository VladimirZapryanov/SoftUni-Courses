# with function
def parking_fee(days, hours_per_day, even_day_odd_hours_price, odd_day_even_hours_price, normal_price):
    all_day_fee = {}
    total_fee = 0
    list_fee = []

    for day in range(1, days + 1):
        day_fee = 0
        for hour in range(1, hours_per_day + 1):
            if day % 2 == 0 and hour % 2 == 1:
                day_fee += even_day_odd_hours_price
            elif day % 2 == 1 and hour % 2 == 0:
                day_fee += odd_day_even_hours_price
            else:
                day_fee += normal_price
        all_day_fee[day] = day_fee

    for k, v in all_day_fee.items():
        total_fee += v
        list_fee.append(f'Day: {k} - {v:.2f} leva')

    return '\n'.join(list_fee) + f'\nTotal: {total_fee:.2f} leva'


days = int(input())
hours_per_day = int(input())
even_day_odd_hours_price = 2.5
odd_day_even_hours_price = 1.25
normal_price = 1

print(parking_fee(days, hours_per_day, even_day_odd_hours_price, odd_day_even_hours_price, normal_price))

# without function
days = int(input())
hours_per_day = int(input())

even_day_odd_hours_price = 2.5
odd_day_even_hours_price = 1.25
normal_price = 1
total_fee = 0

for day in range(1, days + 1):
    day_fee = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 == 1:
            day_fee += even_day_odd_hours_price
        elif day % 2 == 1 and hour % 2 == 0:
            day_fee += odd_day_even_hours_price
        else:
            day_fee += normal_price
    print(f'Day: {day} - {day_fee:.2f} leva')
    total_fee += day_fee

print(f'Total: {total_fee:.2f} leva')


