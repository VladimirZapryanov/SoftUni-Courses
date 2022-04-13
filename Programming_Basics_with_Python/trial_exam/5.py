<<<<<<< HEAD
kg_of_food = int(input()) * 1000
eaten_food = int(input())
count_of_eaten_food = 0

for eaten_food in range(1, eaten_food + eaten_food):
    count_of_eaten_food += eaten_food
    if eaten_food == "Adopted":
        break
left_over_food = kg_of_food - count_of_eaten_food
if kg_of_food >= count_of_eaten_food:
    print(f"Food is enough! Leftovers: {left_over_food} grams.")
else:
=======
kg_of_food = int(input()) * 1000
eaten_food = int(input())
count_of_eaten_food = 0

for eaten_food in range(1, eaten_food + eaten_food):
    count_of_eaten_food += eaten_food
    if eaten_food == "Adopted":
        break
left_over_food = kg_of_food - count_of_eaten_food
if kg_of_food >= count_of_eaten_food:
    print(f"Food is enough! Leftovers: {left_over_food} grams.")
else:
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
    print(f"Food is not enough. You need {abs(left_over_food)} grams more.")