price_of_strawberries = float(input())
kg_of_bananas = float(input())
kg_of_oranges = float(input())
kg_of_raspberries = float(input())
kg_of_strawberries = float(input())
price_of_raspberries = price_of_strawberries * 0.5
price_of_oranges = price_of_raspberries * 0.6
price_of_bananas = price_of_raspberries * 0.2
needed_money = (price_of_bananas * kg_of_bananas) + (price_of_oranges * kg_of_oranges) \
               + (price_of_strawberries * kg_of_strawberries) + (price_of_raspberries * kg_of_raspberries)
print(needed_money)
