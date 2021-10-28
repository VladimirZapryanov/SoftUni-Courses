days = int(input())
food_count = float(input())

biscuit = 0
total_eaten_food = 0
dog_eaten_food = 0
cat_eaten_food = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_eaten_food += dog_food + cat_food
    dog_eaten_food += dog_food
    cat_eaten_food += cat_food

    if day % 3 == 0:
        biscuit += (dog_food + cat_food) * 0.1

eaten_food_percent = (total_eaten_food / food_count) * 100
dog_eaten_food_percent = (dog_eaten_food / total_eaten_food) * 100
cat_eaten_food_percent = (cat_eaten_food / total_eaten_food) * 100

print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{eaten_food_percent:.2f}% of the food has been eaten.")
print(f"{dog_eaten_food_percent:.2f}% eaten from the dog.")
print(f"{cat_eaten_food_percent:.2f}% eaten from the cat.")
