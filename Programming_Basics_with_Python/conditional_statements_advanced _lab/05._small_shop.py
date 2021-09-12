product = input()
town = input()
count = float(input())
price_per_product = 0
if town == "Sofia":
    if product == "coffee":
        price_per_product = 0.50
    elif product == "water":
        price_per_product = 0.80
    elif product == "beer":
        price_per_product = 1.20
    elif product == "sweets":
        price_per_product = 1.45
    elif product == "peanuts":
        price_per_product = 1.60
elif town == "Plovdiv":
    if product == "coffee":
        price_per_product = 0.40
    elif product == "water":
        price_per_product = 0.70
    elif product == "beer":
        price_per_product = 1.15
    elif product == "sweets":
        price_per_product = 1.30
    elif product == "peanuts":
        price_per_product = 1.50
elif town == "Varna":
    if product == "coffee":
        price_per_product = 0.45
    elif product == "water":
        price_per_product = 0.70
    elif product == "beer":
        price_per_product = 1.10
    elif product == "sweets":
        price_per_product = 1.35
    elif product == "peanuts":
        price_per_product = 1.55
final_price = count * price_per_product
print(final_price)