commands = input()
animals = {}


while not commands == "EndDay":
    data = commands.split()
    command = data[0]
    new_data = data[1].split("-")
    animal_name = new_data[0]
    if command == "Add:":
        if new_data[0] not in animals:
            animals[animal_name] = {"needed_food": int(new_data[1]), "area": new_data[2]}
        else:
            animals[animal_name]["needed_food"] += int(new_data[1])

    elif command == "Feed:":
        if animal_name in animals:
            animals[animal_name]["needed_food"] -= int(new_data[1])
        else:
            commands = input()
            continue

        if animals[animal_name]["needed_food"] <= 0:
            print(f"{animal_name} was successfully fed")
            del animals[animal_name]

    commands = input()
    

sorted_animals = dict(sorted(animals.items(), key=lambda kvp: (-kvp[1]["needed_food"], kvp[0])))
print("Animals:")
for el in sorted_animals:
    print(f" {el} -> {sorted_animals[el]['needed_food']}g")

sorted_zone = dict(sorted(animals.items(), key=lambda kvp: (-kpv[1]["area"], kvp[1]["area"])))
print("Areas with hungry animals:")
for el in sorted_zone:
    print(f" {el['area']}: ")
print("Areas with hungry animals:")





