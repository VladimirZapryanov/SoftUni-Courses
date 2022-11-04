flour_price_per_kilogram = float(input())
flour_kilograms = float(input())
sugar_kilograms = float(input())
eggs_box_numbers = int(input())
yeast_packages = int(input())

sugar_price_per_kilogram = flour_price_per_kilogram * 0.75
eggs_box_price = flour_price_per_kilogram * 1.1
yeast_price = sugar_price_per_kilogram * 0.20
flour_cost = flour_price_per_kilogram * flour_kilograms
sugar_cost = sugar_price_per_kilogram * sugar_kilograms
eggs_cost = eggs_box_price * eggs_box_numbers
yeast_cost = yeast_price * yeast_packages
total_cost = flour_cost + sugar_cost + eggs_cost + yeast_cost

print(f'{total_cost:.2f}')
