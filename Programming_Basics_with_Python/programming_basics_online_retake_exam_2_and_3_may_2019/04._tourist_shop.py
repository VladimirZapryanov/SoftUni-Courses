budget = float(input())
command = input()

product_count = 0
all_product_price = 0
need_more_money = False
while not command == 'Stop':
    product_name = command
    product_price = float(input())
    product_count += 1

    if product_count % 3 == 0:
        product_price /= 2
    all_product_price += product_price

    if all_product_price > budget:
        product_count -= 1
        need_more_money = True
        break

    command = input()

if need_more_money:
    needed_money = all_product_price - budget
    print(f"You don't have enough money!")
    print(f'You need {needed_money:.2f} leva!')
else:
    print(f'You bought {product_count} products for {all_product_price:.2f} leva.')