command = input()

resources = {}

while not command == "stop":
    resources_quantity = int(input())
    if command not in resources:
        resources[command] = resources_quantity
    else:
        resources[command] += resources_quantity

    command = input()

for command, resources_quantity in resources.items():
    print(f"{command} -> {resources_quantity}")

