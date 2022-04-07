data = input()

city_info = {}

while not data == "Sail":
    city, population, gold = data.split("||")
    if city not in city_info:
        city_info[city] = {"population": int(population), "gold": int(gold)}
    else:
        city_info[city]["population"] += int(population)
        city_info[city]["gold"] += int(gold)
    data = input()

command = input()

while not command == "End":
    data = command.split("=>")
    if data[0] == "Plunder":
        city_info[data[1]]["population"] -= int(data[2])
        city_info[data[1]]["gold"] -= int(data[3])
        print(f"{data[1]} plundered! {data[3]} gold stolen, {data[2]} citizens killed.")
        if city_info[data[1]]["population"] <= 0 or city_info[data[1]]["gold"] <= 0:
            del city_info[data[1]]
            print(f"{data[1]} has been wiped off the map!")
    elif data[0] == "Prosper":
        if int(data[2]) < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_info[data[1]]["gold"] += int(data[2])
            print(f"{data[2]} gold added to the city treasury. {data[1]} now has {city_info[data[1]]['gold']} gold.")
    command = input()

sorted_city_info = dict(sorted(city_info.items(), key=lambda kvp: (-kvp[1]["gold"], kvp[0])))
if len(sorted_city_info) <= 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(sorted_city_info)} wealthy settlements to go to:")
    for city in sorted_city_info:
        print(f"{city} -> Population: {sorted_city_info[city]['population']} citizens, Gold: {sorted_city_info[city]['gold']} kg")
