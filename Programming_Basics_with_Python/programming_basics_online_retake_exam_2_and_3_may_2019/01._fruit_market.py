price_for_one_kilogram_strawberries = float(input())
kilograms_of_bananas = float(input())
kilograms_of_oranges = float(input())
kilograms_of_raspberries = float(input())
kilograms_of_strawberries = float(input())

price_for_one_kilogram_raspberries = price_for_one_kilogram_strawberries / 2
price_for_one_kilogram_oranges = price_for_one_kilogram_raspberries * 0.6
price_for_one_kilogram_bananas = price_for_one_kilogram_raspberries * 0.2

needed_money = price_for_one_kilogram_strawberries * kilograms_of_strawberries + price_for_one_kilogram_bananas * kilograms_of_bananas \
               + price_for_one_kilogram_oranges * kilograms_of_oranges + price_for_one_kilogram_raspberries * kilograms_of_raspberries
print(f'{needed_money:.2f}')

