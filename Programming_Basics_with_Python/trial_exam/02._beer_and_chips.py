<<<<<<< HEAD
import math
name = input()
budget = float(input())
number_of_beer = int(input())
number_of_chips = int(input())
price_per_all_beer = number_of_beer * 1.20
price_per_all_chips = math.ceil(price_per_all_beer * 0.45 * number_of_chips)
needed_money = price_per_all_beer + price_per_all_chips
left_money = budget - needed_money
if budget >= needed_money:
    print(f"{name} bought a snack and has {left_money:.2f} leva left.")
elif budget < needed_money:
=======
import math
name = input()
budget = float(input())
number_of_beer = int(input())
number_of_chips = int(input())
price_per_all_beer = number_of_beer * 1.20
price_per_all_chips = math.ceil(price_per_all_beer * 0.45 * number_of_chips)
needed_money = price_per_all_beer + price_per_all_chips
left_money = budget - needed_money
if budget >= needed_money:
    print(f"{name} bought a snack and has {left_money:.2f} leva left.")
elif budget < needed_money:
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
    print(f"{name} needs {abs(left_money):.2f} more leva!")