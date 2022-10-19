type_of_drink = input()
sugar_amount = input()
drinks_count = int(input())

total_price = 0
price = 0
if type_of_drink == 'Espresso':
    if sugar_amount == 'Without':
        price = 0.9 * 0.65
    elif sugar_amount == 'Normal':
        price = 1
    elif sugar_amount == 'Extra':
        price = 1.20

    if drinks_count >= 5:
        price = price * 0.75

elif type_of_drink == 'Cappuccino':
    if sugar_amount == 'Without':
        price = 1 * 0.65
    elif sugar_amount == 'Normal':
        price = 1.20
    elif sugar_amount == 'Extra':
        price = 1.60

elif type_of_drink == 'Tea':
    if sugar_amount == 'Without':
        price = 0.50 * 0.65
    elif sugar_amount == 'Normal':
        price = 0.60
    elif sugar_amount == 'Extra':
        price = 0.70

total_price = price * drinks_count
if total_price > 15:
    total_price = total_price * 0.8

print(f'You bought {drinks_count} cups of {type_of_drink} for {total_price:.2f} lv.')