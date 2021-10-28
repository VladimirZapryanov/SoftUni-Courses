all_food_for_dog = int(input())
command = input()
all_food_for_dog_gr = all_food_for_dog * 1000

while not command == "Adopted":
    food_per_day = int(command)
    all_food_for_dog_gr -= food_per_day
    command = input()

if all_food_for_dog_gr >= 0:
    print(f"Food is enough! Leftovers: {all_food_for_dog_gr} grams.")
else:
    print(f"Food is not enough. You need {abs(all_food_for_dog_gr)} grams more.")

