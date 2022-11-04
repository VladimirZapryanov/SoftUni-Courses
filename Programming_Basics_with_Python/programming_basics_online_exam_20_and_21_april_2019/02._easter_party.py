guest_numbers = int(input())
price_per_person = float(input())
budged = float(input())

cake_price = budged * 0.10
all_person_fee = 0
if 10 <= guest_numbers <= 15:
    price_per_person = price_per_person * 0.85
    all_person_fee = price_per_person * guest_numbers
elif 15 < guest_numbers <= 20:
    price_per_person = price_per_person * 0.80
    all_person_fee = price_per_person * guest_numbers
elif guest_numbers > 20:
    price_per_person = price_per_person * 0.75
    all_person_fee = price_per_person * guest_numbers
else:
    all_person_fee = price_per_person * guest_numbers

total_cost = all_person_fee + cake_price
money_difference = budged - total_cost
if budged >= total_cost:
    print(f'It is party time! {money_difference:.2f} leva left.')
else:
    print(f'No party! {abs(money_difference):.2f} leva needed.')