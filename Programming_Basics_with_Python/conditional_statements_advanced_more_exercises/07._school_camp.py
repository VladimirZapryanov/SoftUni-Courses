season = input()
group_type = input()
numbers_of_students = int(input())
number_of_nights = int(input())

price_per_night = 0
sport_type = ''

if season == 'Winter':
    if group_type == 'boys' or group_type == 'girls':
        price_per_night = 9.60
        if group_type == 'boys':
            sport_type = 'Judo'
        elif group_type == 'girls':
            sport_type = 'Gymnastics'
    elif group_type == 'mixed':
        price_per_night = 10
        sport_type = 'Ski'
elif season == 'Spring':
    if group_type == 'boys' or group_type == 'girls':
        price_per_night = 7.20
        if group_type == 'boys':
            sport_type = 'Tennis'
        elif group_type == 'girls':
            sport_type = 'Athletics'
    elif group_type == 'mixed':
        price_per_night = 9.50
        sport_type = 'Cycling'
elif season == 'Summer':
    if group_type == 'boys' or group_type == 'girls':
        price_per_night = 15
        if group_type == 'boys':
            sport_type = 'Football'
        elif group_type == 'girls':
            sport_type = 'Volleyball'
    elif group_type == 'mixed':
        price_per_night = 20
        sport_type = 'Swimming'

hotel_fee = numbers_of_students * number_of_nights * price_per_night

if numbers_of_students >= 50:
    hotel_fee = hotel_fee * 0.5
elif 50 > numbers_of_students >= 20:
    hotel_fee = hotel_fee * 0.85
elif 20 > numbers_of_students >= 10:
    hotel_fee = hotel_fee * 0.95

print(f'{sport_type} {hotel_fee:.2f} lv.')