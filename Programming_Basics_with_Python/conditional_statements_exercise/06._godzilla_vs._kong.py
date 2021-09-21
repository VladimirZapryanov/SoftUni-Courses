budget_for_the_film = float(input())
number_of_extras = int(input())
price_for_clothing = float(input())
decor_price = budget_for_the_film * 0.1
if number_of_extras > 150:
    price_for_clothing = price_for_clothing - (price_for_clothing * 0.1)
all_price_for_clothing = price_for_clothing * number_of_extras
needed_money = all_price_for_clothing + decor_price
left_money = budget_for_the_film - needed_money
if needed_money > budget_for_the_film:
    print("Not enough money!")
    print(f"Wingard needs {abs(left_money):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")