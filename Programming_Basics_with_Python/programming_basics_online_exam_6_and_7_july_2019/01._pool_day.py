from math import ceil

people = int(input())
entrance_fee = float(input())
sun_lounger_price = float(input())
umbrella_price = float(input())

total_entrance_price = people * entrance_fee
total_umbrella_price = ceil((people / 2)) * umbrella_price
total_sun_lounger_price = ceil((people * 0.75)) * sun_lounger_price

total_price_for_all = total_entrance_price + total_umbrella_price + total_sun_lounger_price
print(f'{total_price_for_all:.2f} lv.')
