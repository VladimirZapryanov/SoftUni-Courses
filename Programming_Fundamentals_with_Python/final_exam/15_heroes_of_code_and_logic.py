<<<<<<< HEAD
numbers_of_heroes = int(input())
heroes = {}

for el in range(numbers_of_heroes):
    name, hp, mp = input().split()
    heroes[name] = {"hp": int(hp), "mp": int(mp)}

commands = input()
while not commands == "End":
    data = commands.split(" - ")
    command = data[0]
    hero_name = data[1]

    if command == "CastSpell":
        if heroes[hero_name]["mp"] >= int(data[2]):
            heroes[hero_name]["mp"] -= int(data[2])
            print(f"{hero_name} has successfully cast {data[3]} and now has {heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {data[3]}!")

    elif command == "TakeDamage":
        heroes[hero_name]["hp"] -= int(data[2])
        if heroes[hero_name]["hp"] > 0:
            print(f"{hero_name} was hit for {int(data[2])} HP by {data[3]} and now has {heroes[hero_name]['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {data[3]}!")
            del heroes[hero_name]

    elif command == "Recharge":
        heroes[hero_name]["mp"] += int(data[2])
        if heroes[hero_name]["mp"] > 200:
            print(f"{hero_name} recharged for {int(data[2]) - (heroes[hero_name]['mp'] - 200)} MP!")
            heroes[hero_name]["mp"] = 200
        else:
            print(f"{hero_name} recharged for {int(data[2])} MP!")

    elif command == "Heal":
        heroes[hero_name]["hp"] += int(data[2])
        if heroes[hero_name]["hp"] > 100:
            print(f"{hero_name} healed for {int(data[2]) - (heroes[hero_name]['hp'] - 100)} HP!")
            heroes[hero_name]["hp"] = 100
        else:
            print(f"{hero_name} healed for {int(data[2])} HP!")

    commands = input()
sorted_heroes = dict(sorted(heroes.items(), key=lambda kvp: (-kvp[1]["hp"], kvp[0])))
for hero in sorted_heroes:
=======
numbers_of_heroes = int(input())
heroes = {}

for el in range(numbers_of_heroes):
    name, hp, mp = input().split()
    heroes[name] = {"hp": int(hp), "mp": int(mp)}

commands = input()
while not commands == "End":
    data = commands.split(" - ")
    command = data[0]
    hero_name = data[1]

    if command == "CastSpell":
        if heroes[hero_name]["mp"] >= int(data[2]):
            heroes[hero_name]["mp"] -= int(data[2])
            print(f"{hero_name} has successfully cast {data[3]} and now has {heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {data[3]}!")

    elif command == "TakeDamage":
        heroes[hero_name]["hp"] -= int(data[2])
        if heroes[hero_name]["hp"] > 0:
            print(f"{hero_name} was hit for {int(data[2])} HP by {data[3]} and now has {heroes[hero_name]['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {data[3]}!")
            del heroes[hero_name]

    elif command == "Recharge":
        heroes[hero_name]["mp"] += int(data[2])
        if heroes[hero_name]["mp"] > 200:
            print(f"{hero_name} recharged for {int(data[2]) - (heroes[hero_name]['mp'] - 200)} MP!")
            heroes[hero_name]["mp"] = 200
        else:
            print(f"{hero_name} recharged for {int(data[2])} MP!")

    elif command == "Heal":
        heroes[hero_name]["hp"] += int(data[2])
        if heroes[hero_name]["hp"] > 100:
            print(f"{hero_name} healed for {int(data[2]) - (heroes[hero_name]['hp'] - 100)} HP!")
            heroes[hero_name]["hp"] = 100
        else:
            print(f"{hero_name} healed for {int(data[2])} HP!")

    commands = input()
sorted_heroes = dict(sorted(heroes.items(), key=lambda kvp: (-kvp[1]["hp"], kvp[0])))
for hero in sorted_heroes:
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
    print(f"{hero}\n  HP: {sorted_heroes[hero]['hp']}\n  MP: {sorted_heroes[hero]['mp']}")