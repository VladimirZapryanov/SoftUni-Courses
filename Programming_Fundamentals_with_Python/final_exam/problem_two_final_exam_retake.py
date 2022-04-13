<<<<<<< HEAD
import re

patter = r"(@|#)+(?P<color>[a-z]{3,})(@|#)+[^A-Za-z0-9]+/+(?P<amount>\d+)/+"

text = input()

valid_combination = re.finditer(patter, text)
eggs = []

for match in valid_combination:
    current_match = match.groupdict()
    color = current_match["color"]
    amount = current_match["amount"]
    eggs.append(f"You found {amount} {color} eggs!")

print("\n".join(eggs))
=======
import re

patter = r"(@|#)+(?P<color>[a-z]{3,})(@|#)+[^A-Za-z0-9]+/+(?P<amount>\d+)/+"

text = input()

valid_combination = re.finditer(patter, text)
eggs = []

for match in valid_combination:
    current_match = match.groupdict()
    color = current_match["color"]
    amount = current_match["amount"]
    eggs.append(f"You found {amount} {color} eggs!")

print("\n".join(eggs))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
