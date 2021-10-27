walking_minutes = int(input())
walking_count = int(input())
calories_per_day = int(input())

total_calories = walking_minutes * walking_count * 5

if total_calories >= calories_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")