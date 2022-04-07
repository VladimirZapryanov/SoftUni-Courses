string = input()
commands = input()
new_string = ""

while not commands == "Done":
    data = commands.split()
    command = data[0]
    if command == "TakeOdd":
        for el in range(len(string)):
            if el % 2 == 1:
                new_string += string[el]
        string = new_string
        new_string = ""
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
