from math import ceil

name = input()
budget = float(input())
number_of_beers= int(input())
number_of_chips = int(input())

price_for_all_beer = number_of_beers * 1.20
price_for_all_chips = ceil(price_for_all_beer * 0.45 * number_of_chips)
needed_money = price_for_all_beer + price_for_all_chips
left_money = budget - needed_money

if budget >= needed_money:
    print(f"{name} bought a snack and has {left_money:.2f} leva left.")
elif budget < needed_money:
    print(f"{name} needs {abs(left_money):.2f} more leva!")