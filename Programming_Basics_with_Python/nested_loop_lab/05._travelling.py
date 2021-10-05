destination = input()
while destination != 'End':
    min_budget = float(input())
    needed_money = 0
    while min_budget > needed_money:
        tips = float(input())
        needed_money += tips
    print(f'Going to {destination}!')
    destination = input()


