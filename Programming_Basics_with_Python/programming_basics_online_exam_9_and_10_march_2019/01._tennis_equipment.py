from math import floor, ceil

tennis_racket_price = float(input())
tennis_racket_numbers = int(input())
sneakers_numbers = int(input())

sneakers_price = tennis_racket_price / 6
all_tennis_rackets_price = tennis_racket_price * tennis_racket_numbers
all_sneakers_price = sneakers_price * sneakers_numbers
other_equipment_price = (all_tennis_rackets_price + all_sneakers_price) * 0.2
total_equipment_price = all_tennis_rackets_price + all_sneakers_price + other_equipment_price

djokovic_price = total_equipment_price / 8
sponsors_price = total_equipment_price - djokovic_price

print(f'Price to be paid by Djokovic {floor(djokovic_price)}')
print(f'Price to be paid by sponsors {ceil(sponsors_price)}')
