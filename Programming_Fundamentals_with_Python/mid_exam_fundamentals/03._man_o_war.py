<<<<<<< HEAD
pirate_ship = [int(num) for num in input().split(">")]
warship = [int(num) for num in input().split(">")]
max_health = int(input())
commands = input()
needed_repair = 0
count = 0

while not commands == "Retire":
    data = commands.split()
    command = data[0]

    if command == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if index in range(len(warship)):
            warship_part = int(warship[index])
            warship_part -= damage
            warship.insert(index + 1, warship_part)
            warship.pop(index)

            if warship_part <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
        else:
            commands = input()
            continue

    elif command == "Defend":
        damage = int(data[3])
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
            attack = pirate_ship[start_index:end_index+1]
            for el in attack:
                count += 1
                el = int(el)
                el -= damage
                pirate_ship.insert(start_index + count, el)
                pirate_ship.pop(start_index + count - 1)
                if int(el) <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
        else:
            commands = input()
            continue

    elif command == "Repair":
        index = int(data[1])
        health = int(data[2])
        if 0 <= index <= len(pirate_ship):
            new_health = pirate_ship[index]
            new_health += health
            pirate_ship.insert(index + 1, new_health)
            pirate_ship.pop(index)
            if new_health > max_health:
                new_health = max_health
                pirate_ship.insert(index + 1, new_health)
                pirate_ship.pop(index)
        else:
            commands = input()
            continue

    elif command == "Status":
        for el in pirate_ship:
            if int(el) < max_health * 0.2:
                needed_repair += 1
        print(f"{needed_repair} sections need repair.")

    commands = input()

print(f"Pirate ship status: {sum([int(el) for el in pirate_ship])}")
print(f"Warship status: {sum([int(el) for el in warship])}")
=======
pirate_ship = [int(num) for num in input().split(">")]
warship = [int(num) for num in input().split(">")]
max_health = int(input())
commands = input()
needed_repair = 0
count = 0

while not commands == "Retire":
    data = commands.split()
    command = data[0]

    if command == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if index in range(len(warship)):
            warship_part = int(warship[index])
            warship_part -= damage
            warship.insert(index + 1, warship_part)
            warship.pop(index)

            if warship_part <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
        else:
            commands = input()
            continue

    elif command == "Defend":
        damage = int(data[3])
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
            attack = pirate_ship[start_index:end_index+1]
            for el in attack:
                count += 1
                el = int(el)
                el -= damage
                pirate_ship.insert(start_index + count, el)
                pirate_ship.pop(start_index + count - 1)
                if int(el) <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
        else:
            commands = input()
            continue

    elif command == "Repair":
        index = int(data[1])
        health = int(data[2])
        if 0 <= index <= len(pirate_ship):
            new_health = pirate_ship[index]
            new_health += health
            pirate_ship.insert(index + 1, new_health)
            pirate_ship.pop(index)
            if new_health > max_health:
                new_health = max_health
                pirate_ship.insert(index + 1, new_health)
                pirate_ship.pop(index)
        else:
            commands = input()
            continue

    elif command == "Status":
        for el in pirate_ship:
            if int(el) < max_health * 0.2:
                needed_repair += 1
        print(f"{needed_repair} sections need repair.")

    commands = input()

print(f"Pirate ship status: {sum([int(el) for el in pirate_ship])}")
print(f"Warship status: {sum([int(el) for el in warship])}")
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
