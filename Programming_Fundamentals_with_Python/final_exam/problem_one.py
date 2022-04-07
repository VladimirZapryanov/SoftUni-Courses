string = input()
commands = input()

while not commands == "End":
    data = commands.split()
    command = data[0]
    if command == "Translate":
        string = string.replace((data[1]), data[2])
        print(string)

    elif command == "Includes":
        if data[1] in string:
            print("True")
        else:
            print("False")

    elif command == "Start":
        if string.startswith(data[1]):
            print("True")
        else:
            print("False")

    elif command == "Lowercase":
        string = string.lower()
        print(string)

    elif command == "FindIndex":
        if data[1] in string:
            index = string.rindex(data[1])
            print(index)
        else:
            print(-1)

    elif command == "Remove":
        part_to_remove = string[int(data[1]):int(data[2]) + int(data[1])]
        string = string.replace(part_to_remove, "")
        print(string)

    commands = input()



