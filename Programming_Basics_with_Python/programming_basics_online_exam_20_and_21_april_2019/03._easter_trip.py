trip_destination = input()
trip_date = input()
nights_numbers = int(input())

total_cost = 0
if trip_destination == 'France':
    if trip_date == '21-23':
        night_price = 30
        total_cost = night_price * nights_numbers
    elif trip_date == '24-27':
        night_price = 35
        total_cost = night_price * nights_numbers
    elif trip_date == '28-31':
        night_price = 40
        total_cost = night_price * nights_numbers
elif trip_destination == 'Italy':
    if trip_date == '21-23':
        night_price = 28
        total_cost = night_price * nights_numbers
    elif trip_date == '24-27':
        night_price = 32
        total_cost = night_price * nights_numbers
    elif trip_date == '28-31':
        night_price = 39
        total_cost = night_price * nights_numbers
elif trip_destination == 'Germany':
    if trip_date == '21-23':
        night_price = 32
        total_cost = night_price * nights_numbers
    elif trip_date == '24-27':
        night_price = 37
        total_cost = night_price * nights_numbers
    elif trip_date == '28-31':
        night_price = 43
        total_cost = night_price * nights_numbers

print(f'Easter trip to {trip_destination} : {total_cost:.2f} leva.')