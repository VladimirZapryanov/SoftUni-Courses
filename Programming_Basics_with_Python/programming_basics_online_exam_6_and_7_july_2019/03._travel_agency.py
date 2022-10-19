city_name = input()
type_of_package = input()
vip_pass = input()
days = int(input())

price = 0
if city_name == 'Bansko' or city_name == 'Borovets':
    if type_of_package == 'noEquipment':
        price = 80
        if vip_pass == 'yes':
            price = price * 0.95
    elif type_of_package == 'withEquipment':
        price = 100
        if vip_pass == 'yes':
            price = price * 0.9
elif city_name == 'Varna' or city_name == 'Burgas':
    if type_of_package == 'noBreakfast':
        price = 100
        if vip_pass == 'yes':
            price = price * 0.93
    elif type_of_package == 'withBreakfast':
        price = 130
        if vip_pass == 'yes':
            price = price * 0.88

total_price = 0
if days > 7:
    total_price = price * (days - 1)
else:
    total_price = price * days

if days < 1:
    print('Days must be positive number!')
elif total_price <= 0:
    print('Invalid input!')
else:
    print(f'The price is {total_price:.2f}lv! Have a nice time!')