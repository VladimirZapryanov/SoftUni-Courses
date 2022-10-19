desired_profit = float(input())
command = input()

profit = 0

while not command == 'Party!':
    cocktail_name = command
    numbers_of_cocktails = int(input())
    price_of_cocktails = int(len(cocktail_name))
    order_price = price_of_cocktails * numbers_of_cocktails
    if order_price % 2 == 1:
        order_price = order_price * 0.75
    profit += order_price

    if desired_profit <= profit:
        break

    command = input()

if desired_profit <= profit:
    print('Target acquired.')
else:
    print(f'We need {desired_profit - profit:.2f} leva more.')

print(f'Club income - {profit:.2f} leva.')