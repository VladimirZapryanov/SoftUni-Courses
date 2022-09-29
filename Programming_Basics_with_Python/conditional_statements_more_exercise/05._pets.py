from math import floor, ceil


def pets_food(days, food_in_kg, dog_food_per_dey_kg, cat_food_per_dey_kg, turtle_food_per_dey_gr):
    turtle_food_per_dey_kg = turtle_food_per_dey_gr / 1000
    pets_needed_food_per_day = dog_food_per_dey_kg + cat_food_per_dey_kg + turtle_food_per_dey_kg
    pets_needed_food_for_all_days = days * pets_needed_food_per_day
    food_difference = food_in_kg - pets_needed_food_for_all_days

    if food_difference >= 0:
        return f'{floor(food_difference)} kilos of food left.'
    else:
        return f'{ceil(abs(food_difference))} more kilos of food are needed.'


days = int(input())
food_in_kg = int(input())
dog_food_per_dey_kg = float(input())
cat_food_per_dey_kg = float(input())
turtle_food_per_dey_gr = float(input())

print(pets_food(days, food_in_kg, dog_food_per_dey_kg, cat_food_per_dey_kg, turtle_food_per_dey_gr))