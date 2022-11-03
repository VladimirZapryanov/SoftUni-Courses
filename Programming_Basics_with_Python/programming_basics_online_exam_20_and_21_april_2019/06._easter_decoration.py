customers_numbers = int(input())
basket_price = 1.50
wreath_price = 3.80
chocolate_bunny_price = 7

total_money = 0
for _ in range(customers_numbers):
    command = input()
    current_items_count = 0
    current_money = 0

    while not command == 'Finish':
        item = command
        current_items_count += 1

        if item == 'basket':
            current_money += basket_price
        elif item == 'chocolate bunny':
            current_money += chocolate_bunny_price
        elif item == 'wreath':
            current_money += wreath_price

        command = input()

    if current_items_count % 2 == 0:
        current_money = current_money * 0.80

    total_money += current_money

    print(f'You purchased {current_items_count} items for {current_money:.2f} leva.')

average_bill = total_money / customers_numbers
print(f'Average bill per client is: {average_bill:.2f} leva.')


