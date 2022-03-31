import re

pattern = r"(?P<separator>=|/)(?P<destination>[A-Z]+[A-Za-z]{2,})(?P=separator)"

text = input()

valid_destination = re.finditer(pattern, text)

travel_points = 0
destinations = []

for match in valid_destination:
    current_match = match.groupdict()
    destinations.append(current_match["destination"])
    travel_points += len(current_match["destination"])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")