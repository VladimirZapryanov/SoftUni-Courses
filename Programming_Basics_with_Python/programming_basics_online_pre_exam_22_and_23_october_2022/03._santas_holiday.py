days = int(input())
type_of_room = input()
score = input()

nights = days - 1
room_price = 0

if type_of_room == 'room for one person':
    room_price = nights * 18.00
elif type_of_room == 'apartment':
    room_price = nights * 25.00
    if days < 10:
        room_price = room_price * 0.70
    elif 10 <= days <= 15:
        room_price = room_price * 0.65
    elif days > 15:
        room_price = room_price * 0.50
elif type_of_room == 'president apartment':
    room_price = nights * 35.00
    if days < 10:
        room_price = room_price * 0.90
    elif 10 <= days <= 15:
        room_price = room_price * 0.85
    elif days > 15:
        room_price = room_price * 0.80

if score == 'positive':
    room_price = room_price * 1.25
elif score == 'negative':
    room_price = room_price * 0.9

print(f'{room_price:.2f}')