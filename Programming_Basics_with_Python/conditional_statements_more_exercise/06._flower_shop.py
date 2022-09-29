from math import floor, ceil


def get_present(magnolias_count, hyacinths_count, roses_count, cacti_count, present_price, magnolias_price, hyacinths_price, roses_price, cacti_price, fee):
    total_profit = magnolias_count * magnolias_price + hyacinths_count * hyacinths_price + roses_count * roses_price + cacti_count * cacti_price
    total_profit_after_fee = total_profit - total_profit * fee
    money_difference = total_profit_after_fee - present_price

    if total_profit_after_fee >= present_price:
        return f'She is left with {floor(money_difference)} leva.'
    else:
        return f'She will have to borrow {ceil(abs(money_difference))} leva.'


magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
present_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cacti_price = 8
fee = 5 / 100

print(get_present(magnolias_count, hyacinths_count, roses_count, cacti_count, present_price, magnolias_price, hyacinths_price, roses_price, cacti_price, fee))