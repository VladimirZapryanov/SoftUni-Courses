<<<<<<< HEAD
string = input()
commands = input()

while not commands == "Done":
    data = commands.split()
    command = data[0]
    if command == "TakeOdd":
        string = "".join([string[el] for el in range(len(string)) if el % 2 == 1])
        print(string)

    elif command == "Cut":
        left_part = string[:int(data[1])]
        right_part = string[int(data[1]) + int(data[2]):]
        string = left_part + right_part
        print(string)

    elif command == "Substitute":
        if data[1] in string:
            string = string.replace(data[1], data[2])
            print(string)
        else:
            print("Nothing to replace!")

    commands = input()

print(f"Your password is: {string}")
=======
string = input()
commands = input()

while not commands == "Done":
    data = commands.split()
    command = data[0]
    if command == "TakeOdd":
        string = "".join([string[el] for el in range(len(string)) if el % 2 == 1])
        print(string)

    elif command == "Cut":
        left_part = string[:int(data[1])]
        right_part = string[int(data[1]) + int(data[2]):]
        string = left_part + right_part
        print(string)

    elif command == "Substitute":
        if data[1] in string:
            string = string.replace(data[1], data[2])
            print(string)
        else:
            print("Nothing to replace!")

    commands = input()

print(f"Your password is: {string}")
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
