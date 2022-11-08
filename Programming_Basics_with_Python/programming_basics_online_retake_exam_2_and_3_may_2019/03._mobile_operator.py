contract_term = input()
type_of_contract = input()
added_mobile_internet = input()
number_of_months_to_pay = int(input())

price_per_month = 0
if contract_term == 'one':
    if type_of_contract == 'Small':
        price_per_month = 9.98
    elif type_of_contract == 'Middle':
        price_per_month = 18.99
    elif type_of_contract == 'Large':
        price_per_month = 25.98
    elif type_of_contract == 'ExtraLarge':
        price_per_month = 35.99
elif contract_term == 'two':
    if type_of_contract == 'Small':
        price_per_month = 8.58
    elif type_of_contract == 'Middle':
        price_per_month = 17.09
    elif type_of_contract == 'Large':
        price_per_month = 23.59
    elif type_of_contract == 'ExtraLarge':
        price_per_month = 31.79

if added_mobile_internet == 'yes':
    if price_per_month <= 10:
        price_per_month += 5.50
    elif price_per_month <= 30:
        price_per_month += 4.35
    else:
        price_per_month += 3.85

money_for_pay = number_of_months_to_pay * price_per_month
if contract_term == 'two':
    money_for_pay = money_for_pay * 0.9625
print(f'{money_for_pay:.2f} lv.')