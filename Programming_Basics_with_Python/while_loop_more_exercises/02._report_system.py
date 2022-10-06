needed_money = int(input())
command = input()

cash_payment = 0
cash_payment_count = 0
card_payment = 0
card_payment_count = 0
count = 0
enough_money = False

while not command == 'End':
    count += 1
    money = int(command)
    if count % 2 == 1:
        if money > 100:
            print('Error in transaction!')
        else:
            cash_payment += money
            cash_payment_count += 1
            needed_money -= money
            print('Product sold!')

    else:
        if money < 10:
            print('Error in transaction!')
        else:
            card_payment += money
            card_payment_count += 1
            needed_money -= money
            print('Product sold!')

    if needed_money <= 0:
        enough_money = True
        break

    command = input()
if enough_money:
    print(f'Average CS: {cash_payment / cash_payment_count:.2f}')
    print(f'Average CC: {card_payment / card_payment_count:.2f}')
else:
    print('Failed to collect required money for charity.')