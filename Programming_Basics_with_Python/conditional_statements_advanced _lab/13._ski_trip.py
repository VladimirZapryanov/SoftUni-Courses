days = int(input())
type_of_room = input()
opinion = input()
nights = days - 1
price_per_night = 0
if type_of_room == "room for one person":
    price_per_night = 18
elif type_of_room == "apartment":
    price_per_night = 25
elif type_of_room == "president apartment":
    price_per_night = 35
total_price = nights * price_per_night
if type_of_room == "apartment":
    if days < 10:
        total_price = total_price - 0.3 * total_price
    elif 10 <= days <= 15:
        total_price = total_price - 0.35 * total_price
    elif days > 15:
        total_price = total_price - 0.5 * total_price
elif type_of_room == "president apartment":
    if days < 10:
        total_price = total_price - 0.1 * total_price
    elif 10 <= days <= 15:
        total_price = total_price - 0.15 * total_price
    elif days > 15:
        total_price = total_price - 0.2 * total_price
if opinion == "positive":
    total_price = total_price + 0.25 * total_price
elif opinion == "negative":
    total_price = total_price - 0.1 * total_price
print(f"{total_price:.2f}")


