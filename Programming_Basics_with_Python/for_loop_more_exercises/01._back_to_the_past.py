legacy_money = float(input())
year_to_live = int(input())

money_cost_per_year = 12000
ivan_years = 18
back_to_past = 1800

for year in range(back_to_past, year_to_live + 1):
    if year % 2 == 0:
        legacy_money -= money_cost_per_year
    else:
        legacy_money -= money_cost_per_year + (50 * ivan_years)
    ivan_years += 1

if legacy_money >= 0:
    print(f'Yes! He will live a carefree life and will have {legacy_money:.2f} dollars left.')
else:
    print(f'He will need {abs(legacy_money):.2f} dollars to survive.')