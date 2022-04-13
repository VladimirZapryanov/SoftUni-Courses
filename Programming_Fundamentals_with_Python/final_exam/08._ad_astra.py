<<<<<<< HEAD
import re

pattern = r"(?P<separator>\||\#)(?P<item>[A-Za-z\s]+)(?P=separator)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(?P=separator)(?P<calories>[0-9]+)(?P=separator)"

text = input()
total_calories = 0
needed_calories = 2000
food_info = []

valid_matches = re.finditer(pattern, text)

for match in valid_matches:
    current_match = match.groupdict()
    calories = int(current_match["calories"])
    total_calories += calories
    food_info.append(f"Item: {current_match['item']}, Best before: {current_match['date']}, Nutrition: {current_match['calories']}")

left_days = total_calories // needed_calories

print(f"You have food to last you for: {left_days} days!")
print("\n".join(food_info))
=======
import re

pattern = r"(?P<separator>\||\#)(?P<item>[A-Za-z\s]+)(?P=separator)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(?P=separator)(?P<calories>[0-9]+)(?P=separator)"

text = input()
total_calories = 0
needed_calories = 2000
food_info = []

valid_matches = re.finditer(pattern, text)

for match in valid_matches:
    current_match = match.groupdict()
    calories = int(current_match["calories"])
    total_calories += calories
    food_info.append(f"Item: {current_match['item']}, Best before: {current_match['date']}, Nutrition: {current_match['calories']}")

left_days = total_calories // needed_calories

print(f"You have food to last you for: {left_days} days!")
print("\n".join(food_info))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
