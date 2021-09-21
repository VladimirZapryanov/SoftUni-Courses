price_of_trip = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
profit_from_puzzles = number_of_puzzles * 2.60
profit_from_dolls = number_of_dolls * 3
profit_from_teddy_bears = number_of_teddy_bears * 4.10
profit_from_minions = number_of_minions * 8.20
profit_from_trucks = number_of_trucks * 2
total_profit = profit_from_puzzles + profit_from_dolls + profit_from_teddy_bears \
    + profit_from_minions + profit_from_trucks
total_toys = number_of_puzzles + number_of_dolls + number_of_teddy_bears \
    + number_of_minions + number_of_trucks
if total_toys >= 50:
    total_profit = total_profit - (total_profit * 0.25)
rent_for_shop = total_profit * 0.1
final_money = total_profit - rent_for_shop
left_money = final_money - price_of_trip
if final_money >= price_of_trip:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(F"Not enough money! {abs(left_money):.2f} lv needed.")