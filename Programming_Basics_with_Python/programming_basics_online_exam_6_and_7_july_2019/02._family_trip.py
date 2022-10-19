budget = float(input())
nights_number = int(input())
price_per_night = float(input())
percent_other_fee = int(input())

if nights_number > 7:
    price_per_night = price_per_night * 0.95

all_nights_price = price_per_night * nights_number
other_fee = budget * (percent_other_fee / 100)
total_fee = all_nights_price + other_fee

if total_fee <= budget:
    print(f'Ivanovi will be left with {budget - total_fee:.2f} leva after vacation.')
else:
    print(f'{total_fee - budget:.2f} leva needed.')