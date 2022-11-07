voucher_amount = int(input())
command = input()

tickets_count = 0
other_products_count = 0
while not command == 'End':
    product = command
    current_product_price = 0
    is_ticket = False

    if len(product) > 8:
        is_ticket = True
        current_product_price = ord(product[0]) + ord(product[1])
    else:
        current_product_price = ord(product[0])

    if voucher_amount - current_product_price >= 0:
        voucher_amount -= current_product_price
        if is_ticket:
            tickets_count += 1
        else:
            other_products_count += 1
    else:
        break

    command = input()

print(tickets_count)
print(other_products_count)
