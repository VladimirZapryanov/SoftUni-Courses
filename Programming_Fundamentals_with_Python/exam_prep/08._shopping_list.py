groceries = input().split("!")

data = input()

while not data == "Go Shopping!":
    data = data.split()
    if data[0] == "Urgent" and data[1] not in groceries:
        groceries.insert(0, data[1])
    elif data[0] == "Unnecessary" and data[1] in groceries:
        groceries.remove(data[1])
    elif data[0] == "Correct" and data[1] in groceries:
        index = groceries.index(data[1])
        groceries.remove(data[1])
        groceries.insert(index, data[2])
    elif data[0] == "Rearrange" and data[1] in groceries:
        groceries.append(data[1])
        groceries.remove(data[1])
    data = input()

print(", ".join(groceries))
