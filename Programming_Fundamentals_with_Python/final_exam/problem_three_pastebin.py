animals = {}
areas = {}
command = input()

while not command == 'EndDay':
    command = command.split(': ')
    if command[0] == 'Add':
        name, food, area = command[1].split('-')
        if name not in animals:
            animals[name] = 0
        animals[name] += int(food)
        if area not in areas:
            areas[area] = []
        if name not in areas[area]:
            areas[area].append(name)
    elif command[0] == 'Feed':
        name, food = command[1].split('-')
        if name in animals:
            animals[name] -= int(food)
            if animals[name] <= 0:
                animals.pop(name)
                print(f'{name} was successfully fed')
                for k, v in areas.items():
                    if name in v:
                        areas[k].remove(name)
    command = input()

areas = {k: v for (k, v) in areas.items() if len(v) > 0}

print('Animals:')
for k, v in sorted(animals.items(), key=lambda kvp: (-kvp[1], kvp[0])): print(f' {k} -> {v}g')
print('Areas with hungry animals:')
for k, v in sorted(areas.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    print(f' {k}: {len(v)}')