fruit = input()
day_of_week = input()
quantity = float(input())
price_per_product = 0
if not day_of_week in ("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"):
    print("error")
    exit()
if not fruit in ("banana, apple, orange, grapefruit, kiwi, pineapple, grapes"):
    print("error")
    exit()
if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        price_per_product = 2.50
    elif fruit == "apple":
        price_per_product = 1.20
    elif fruit == "orange":
        price_per_product = 0.85
    elif fruit == "grapefruit":
        price_per_product = 1.45
    elif fruit == "kiwi":
        price_per_product = 2.70
    elif fruit == "pineapple":
        price_per_product = 5.50
    elif fruit == "grapes":
        price_per_product = 3.85
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price_per_product = 2.7
    elif fruit == "apple":
        price_per_product = 1.25
    elif fruit == "orange":
        price_per_product = 0.90
    elif fruit == "grapefruit":
        price_per_product = 1.60
    elif fruit == "kiwi":
        price_per_product = 3.00
    elif fruit == "pineapple":
        price_per_product = 5.60
    elif fruit == "grapes":
        price_per_product = 4.20
total_price = (price_per_product * quantity)
print(f"{total_price:.2f}")