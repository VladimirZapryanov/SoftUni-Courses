initial_loot = input().split("|")
commands = input()
steal_loot = []

while not commands == "Yohoho!":
    data = commands.split()
    command = data[0]
    if command == "Loot":
        del data[0]
        for el in data:
            if el not in initial_loot:
                initial_loot.insert(0, el)

    elif command == "Drop":
        index = int(data[1])
        if 0 <= index < len(initial_loot):
            new_word = initial_loot[index]
            initial_loot.append(new_word)
            initial_loot.pop(index)

    elif command == "Steal":
        count = int(data[1])
        if count >= len(initial_loot):
            print(", ".join(initial_loot))
            initial_loot = []
        else:
            print(", ".join(initial_loot[len(initial_loot) - count:]))
            initial_loot = initial_loot[:len(initial_loot) - count]

    commands = input()

all_gain = 0
el_count = 0

if len(initial_loot) == 0:
    print("Failed treasure hunt.")

else:
    for el in initial_loot:
        el_count += 1
        all_gain += len(el)

    average_gain = all_gain / el_count

    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")