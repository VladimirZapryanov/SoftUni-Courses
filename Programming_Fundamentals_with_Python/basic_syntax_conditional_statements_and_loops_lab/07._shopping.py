budget = int(input())
command = input()

you_buy_everything = True
while not command == 'End':
    price = int(command)
    if budget >= price:
        budget -= price
    else:
        print('You went in overdraft!')
        you_buy_everything = False
        break

    command = input()

if you_buy_everything:
    print('You bought everything needed.')

