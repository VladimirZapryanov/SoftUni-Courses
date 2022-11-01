stage_of_championship = input()
type_of_ticket = input()
tickets_number = int(input())
trophy_photo = input()

price = 0
if stage_of_championship == 'Quarter final':
    if type_of_ticket == 'Standard':
        price = tickets_number * 55.50
    elif type_of_ticket == 'Premium':
        price = tickets_number * 105.20
    elif type_of_ticket == 'VIP':
        price = tickets_number * 118.90
elif stage_of_championship == 'Semi final':
    if type_of_ticket == 'Standard':
        price = tickets_number * 75.88
    elif type_of_ticket == 'Premium':
        price = tickets_number * 125.22
    elif type_of_ticket == 'VIP':
        price = tickets_number * 300.40
elif stage_of_championship == 'Final':
    if type_of_ticket == 'Standard':
        price = tickets_number * 110.10
    elif type_of_ticket == 'Premium':
        price = tickets_number * 160.66
    elif type_of_ticket == 'VIP':
        price = tickets_number * 400

final_price = 0
if price > 4000:
    final_price = price * 0.75
elif price > 2500:
    final_price = price * 0.9
else:
    final_price = price

if price <= 4000 and trophy_photo == 'Y':
    final_price += tickets_number * 40

print(f'{final_price:.2f}')

