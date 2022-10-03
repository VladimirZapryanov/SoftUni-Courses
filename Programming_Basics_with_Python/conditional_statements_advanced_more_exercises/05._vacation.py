budget = float(input())
season = input()

place_to_stay = ''
country_to_go = ''
money_cost = 0

if budget <= 1000:
    place_to_stay = 'Camp'
    if season == 'Summer':
        country_to_go = 'Alaska'
        money_cost = budget * 0.65
    elif season == 'Winter':
        country_to_go = 'Morocco'
        money_cost = budget * 0.45
elif 1000 < budget <= 3000:
    place_to_stay = 'Hut'
    if season == 'Summer':
        country_to_go = 'Alaska'
        money_cost = budget * 0.80
    elif season == 'Winter':
        country_to_go = 'Morocco'
        money_cost = budget * 0.60
elif budget > 3000:
    place_to_stay = 'Hotel'
    money_cost = budget * 0.90
    if season == 'Summer':
        country_to_go = 'Alaska'
    elif season == 'Winter':
        country_to_go = 'Morocco'

print(f'{country_to_go} - {place_to_stay} - {money_cost:.2f}')

