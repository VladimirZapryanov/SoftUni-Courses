cats_numbers = int(input())

one_kilograms_food_price = 12.45
small_cat_count = 0
big_cat_count = 0
huge_cat_count = 0
total_eaten_food_per_day = 0

for c in range(cats_numbers):
    food_per_cat = float(input())
    total_eaten_food_per_day += food_per_cat

    if 100 <= food_per_cat < 200:
        small_cat_count += 1
    elif 200 <= food_per_cat < 300:
        big_cat_count += 1
    elif 300 <= food_per_cat < 400:
        huge_cat_count += 1

price_for_food_per_day = (total_eaten_food_per_day / 1000) * one_kilograms_food_price
print(f"Group 1: {small_cat_count} cats.")
print(f"Group 2: {big_cat_count} cats.")
print(f"Group 3: {huge_cat_count} cats.")
print(f"Price for food per day: {price_for_food_per_day:.2f} lv.")


