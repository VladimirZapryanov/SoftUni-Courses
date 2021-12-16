items = input().split(", ")
data = input()

while not data == "Craft!":
    command = data.split(" - ")
    if command[0] == "Collect":
        if command[1] in items:
            continue
        else:
            items.append(command[1])
    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == "Combine Items":
        new_items = command[1].split(":")
        if new_items[0] in items:
            item_index = items.index(new_items[0])
            items.insert(item_index + 1, new_items[1])
    elif command[0] == "Renew":
        if command[1] in items:
            items.append(command[1])
            items.remove(command[1])
    data = input()

print(", ".join(items))
