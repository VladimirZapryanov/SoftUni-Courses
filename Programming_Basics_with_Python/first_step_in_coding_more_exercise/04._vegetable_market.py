def profit_in_euro(vegetable_price, fruits_price, vegetable_kilograms, fruits_kilograms, euro_value):
    profit_in_leva = (vegetable_price * vegetable_kilograms) + (fruits_price * fruits_kilograms)
    return f'{profit_in_leva / euro_value:.2f}'


vegetable_price = float(input())
fruits_price = float(input())
vegetable_kilograms = float(input())
fruits_kilograms = float(input())
euro_value = 1.94

print(profit_in_euro(vegetable_price, fruits_price, vegetable_kilograms, fruits_kilograms, euro_value))
