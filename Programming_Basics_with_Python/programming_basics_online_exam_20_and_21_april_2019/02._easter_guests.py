from math import ceil


def easter_guests(guests_numbers, budget, easter_bread_price, egg_price):
    needed_easter_breads = ceil(guests_numbers / 3)
    needed_eggs = guests_numbers * 2
    needed_money = (needed_eggs * egg_price) + (needed_easter_breads * easter_bread_price)
    money_difference = budget - needed_money

    if needed_money <= budget:
        return f'Lyubo bought {needed_easter_breads} Easter bread and {needed_eggs} eggs.\nHe has {money_difference:.2f} lv. left.'
    else:
        return f"Lyubo doesn't have enough money.\nHe needs {abs(money_difference):.2f} lv. more."


guests_numbers = int(input())
budget = int(input())

easter_bread_price = 4
egg_price = 0.45

print(easter_guests(guests_numbers, budget, easter_bread_price, egg_price))
