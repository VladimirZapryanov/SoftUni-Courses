budget = int(input())
season = input()
fishers = int(input())
boat_price = 0
if season == "Spring":
    boat_price = 3000
    if fishers <= 6:
        boat_price -= 0.1 * boat_price
    elif 6 < fishers <= 11:
        boat_price -= 0.15 * boat_price
    elif fishers > 12:
        boat_price -= 0.25 * boat_price
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
    if fishers <= 6:
        boat_price -= 0.1 * boat_price
    elif 6 < fishers <= 11:
        boat_price -= 0.15 * boat_price
    elif fishers > 12:
        boat_price -= 0.25 * boat_price
elif season == "Winter":
    boat_price = 2600
    if fishers <= 6:
        boat_price -= 0.1 * boat_price
    elif 6 < fishers <= 11:
        boat_price -= 0.15 * boat_price
    elif fishers > 12:
        boat_price -= 0.25 * boat_price
if fishers % 2 == 0 and season != "Autumn":
    discount = 0.05 * boat_price
    boat_price -= discount
if budget >= boat_price:
    diff = budget - boat_price
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    diff = boat_price - budget
    print(f"Not enough money! You need {diff:.2f} leva.")