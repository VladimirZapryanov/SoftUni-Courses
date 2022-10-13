def money_combinator(one_lv_coins, two_lv_coins, five_lv_banknotes, money_amount):
    all_combinations = []

    for olc in range(0, one_lv_coins + 1):
        for tlc in range(0, two_lv_coins + 1):
            for flb in range(0, five_lv_banknotes + 1):
                if olc + (tlc * 2) + (flb * 5) == money_amount:
                    all_combinations.append(f'{olc} * 1 lv. + {tlc} * 2 lv. + {flb} * 5 lv. = {money_amount} lv.')

    return '\n'.join(all_combinations)


one_lv_coins = int(input())
two_lv_coins = int(input())
five_lv_banknotes = int(input())
money_amount = int(input())

print(money_combinator(one_lv_coins, two_lv_coins, five_lv_banknotes, money_amount))
