needed_money = int(input())
command = input()

profit = 0
while not command == 'closed':
    type_of_service = command

    if type_of_service == 'haircut':
        type_of_haircut = input()
        if type_of_haircut == 'mens':
            profit += 15
        elif type_of_haircut == 'ladies':
            profit += 20
        elif type_of_haircut == 'kids':
            profit += 10
    elif type_of_service == 'color':
        type_of_color = input()
        if type_of_color == 'touch up':
            profit += 20
        elif type_of_color == 'full color':
            profit += 30

    if profit >= needed_money:
        break

    command = input()

if profit >= needed_money:
    print('You have reached your target for the day!')
else:
    print(f'Target not reached! You need {needed_money - profit}lv. more.')

print(f'Earned money: {profit}lv.')