<<<<<<< HEAD
data = [int(num) for num in input().split(" ")]
commands = input()
el_count = 0

while not commands == "end":
    new_data = commands.split()
    command = new_data[0]

    if command == "swap":
        index_one = int(new_data[1])
        index_two = int(new_data[2])
        data[index_one], data[index_two] = data[index_two], data[index_one]

    elif command == "multiply":
        index_one = int(new_data[1])
        index_two = int(new_data[2])
        new_index = data[index_one] * data[index_two]
        data.insert(index_one + 1, new_index)
        data.pop(index_one)

    elif command == "decrease":
        data = [el - 1 for el in data]

    commands = input()

print(", ".join(str(el) for el in data))

=======
data = [int(num) for num in input().split(" ")]
commands = input()
el_count = 0

while not commands == "end":
    new_data = commands.split()
    command = new_data[0]

    if command == "swap":
        index_one = int(new_data[1])
        index_two = int(new_data[2])
        data[index_one], data[index_two] = data[index_two], data[index_one]

    elif command == "multiply":
        index_one = int(new_data[1])
        index_two = int(new_data[2])
        new_index = data[index_one] * data[index_two]
        data.insert(index_one + 1, new_index)
        data.pop(index_one)

    elif command == "decrease":
        data = [el - 1 for el in data]

    commands = input()

print(", ".join(str(el) for el in data))

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
