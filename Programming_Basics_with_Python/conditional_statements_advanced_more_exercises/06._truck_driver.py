season = input()
km_per_month = float(input())

season_months = 4
profit_per_month = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        profit_per_month = km_per_month * 0.75
    elif season == 'Summer':
        profit_per_month = km_per_month * 0.90
    elif season == 'Winter':
        profit_per_month = km_per_month * 1.05

elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        profit_per_month = km_per_month * 0.95
    elif season == 'Summer':
        profit_per_month = km_per_month * 1.10
    elif season == 'Winter':
        profit_per_month = km_per_month * 1.25

elif 10000 < km_per_month <= 20000:
    profit_per_month = km_per_month * 1.45

final_profit = (profit_per_month * season_months) * 0.9

print(f'{final_profit:.2f}')