budget = float(input())
needed_litters_of_fuel = float(input())
day_of_week = input()

price_per_one_litter_fuel = 2.10
price_for_tour_guide = 100
saturday_discount = 0.10
sunday_discount = 0.20

needed_money = needed_litters_of_fuel * price_per_one_litter_fuel + price_for_tour_guide
if day_of_week == 'Saturday':
    needed_money = needed_money - (needed_money * saturday_discount)
elif day_of_week == 'Sunday':
    needed_money = needed_money - (needed_money * sunday_discount)

money_difference = budget - needed_money
if money_difference >= 0:
    print(f'Safari time! Money left: {money_difference:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {abs(money_difference):.2f} lv.')

