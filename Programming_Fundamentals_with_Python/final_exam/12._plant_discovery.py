numbers_of_lines = int(input())
plants_info = {}

for n in range(numbers_of_lines):
    plant, rarity = input().split("<->")
    if plant not in plants_info:
        plants_info[plant] = {"rarity": int(rarity), "rating": 0}
    else:
        plants_info[plant][rarity] += int(rarity)

commands = input()
while not commands == "Exhibition":
    data = commands.split()
    command = data[0]
    plant = data[1]
    if plant not in plants_info:
        print("error")
    if command == "Rate:":
        if not plants_info[plant]["rating"] == 0:
            plants_info[plant]["rating"] = float(plants_info[plant]["rating"] / 2) + float(int(data[3]) / 2)
        else:
            plants_info[plant]["rating"] += int(data[3])

    elif command == "Update:":
        plants_info[plant]["rarity"] = int(data[3])

    elif command == "Reset:":
        plants_info[plant]["rating"] = 0

    elif not command == "Rate:" or not command == "Update:" or not command == "Reset:":
        print("error")

    commands = input()

sorted_plants_info = dict(sorted(plants_info.items(), key=lambda kvp: (-kvp[1]["rarity"], -kvp[1]["rating"])))

print("Plants for the exhibition:")
for el in sorted_plants_info:
    print(f"- {el}; Rarity: {sorted_plants_info[el]['rarity']}; Rating: {sorted_plants_info[el]['rating']:.2f}")
