<<<<<<< HEAD
commands = input()
shop = {}
all_sold = 0

while not commands == "Complete":
    command, quantity, food = commands.split()
    if command == "Receive":
        if int(quantity) <= 0:
            commands = input()
            continue
        if food not in shop:
            shop[food] = int(quantity)
        else:
            shop[food] += int(quantity)

    elif command == "Sell":
        if food not in shop:
            print(f"You do not have any {food}.")
        elif shop[food] < int(quantity):
            print(f"There aren't enough {food}. You sold the last {shop[food]} of them.")
            all_sold += shop[food]
            del shop[food]
        else:
            shop[food] -= int(quantity)
            all_sold += int(quantity)
            print(f"You sold {int(quantity)} {food}.")
            if shop[food] == 0:
                del shop[food]

    commands = input()

sorted_shop = dict(sorted(shop.items(), key=lambda kvp: kvp[0]))
for el in sorted_shop:
    print(f"{el}: {shop[el]}")

=======
commands = input()
shop = {}
all_sold = 0

while not commands == "Complete":
    command, quantity, food = commands.split()
    if command == "Receive":
        if int(quantity) <= 0:
            commands = input()
            continue
        if food not in shop:
            shop[food] = int(quantity)
        else:
            shop[food] += int(quantity)

    elif command == "Sell":
        if food not in shop:
            print(f"You do not have any {food}.")
        elif shop[food] < int(quantity):
            print(f"There aren't enough {food}. You sold the last {shop[food]} of them.")
            all_sold += shop[food]
            del shop[food]
        else:
            shop[food] -= int(quantity)
            all_sold += int(quantity)
            print(f"You sold {int(quantity)} {food}.")
            if shop[food] == 0:
                del shop[food]

    commands = input()

sorted_shop = dict(sorted(shop.items(), key=lambda kvp: kvp[0]))
for el in sorted_shop:
    print(f"{el}: {shop[el]}")

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
print(f"All sold: {all_sold} goods")