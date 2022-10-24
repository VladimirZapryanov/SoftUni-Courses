budget = float(input())
destination = input()
season = input()
days = int(input())

needed_money = 0
if destination == 'Dubai':
    if season == 'Winter':
        needed_money = 45000 * days
    elif season == 'Summer':
        needed_money = 40000 * days

    needed_money = needed_money * 0.70
elif destination == 'Sofia':
    if season == 'Winter':
        needed_money = 17000 * days
    elif season == 'Summer':
        needed_money = 12500 * days

    needed_money = needed_money * 1.25
elif destination == 'London':
    if season == 'Winter':
        needed_money = 24000 * days
    elif season == 'Summer':
        needed_money = 20250 * days

money_difference = budget - needed_money
if budget >= needed_money:
    print(f'The budget for the movie is enough! We have {money_difference:.2f} leva left!')
else:
    print(f'The director needs {abs(money_difference):.2f} leva more!')