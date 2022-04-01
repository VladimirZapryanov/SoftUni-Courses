import re

email = input()
commands = input()

while not commands == "Valid":
    data = commands.split()
    command = data[0]

    if command == "Upper":
        index = int(data[1])
        left_indexes = email[:index]
        right_indexes = email[index + 1:]
        searched_index = email[index:index+1]
        searched_index = searched_index.upper()
        email = left_indexes + searched_index + right_indexes
        print(email)

    elif command == "Lower":
        index_one = int(data[1])
        left_indexes = email[:index_one]
        right_indexes = email[index_one + 1:]
        searched_index = email[index_one:index_one + 1]
        searched_index = searched_index.lower()
        email = left_indexes + searched_index + right_indexes
        print(email)

    elif command == "Insert":
        index_two = int(data[1])
        char = data[2]
        left_indexes = email[:index_two]
        right_indexes = email[index_two + 1:]
        email = left_indexes + char + right_indexes
        print(email)

    elif command == "Change":
        char_one = data[1]
        value = int(data[2])
        if char_one in email:
            new_char = chr(ord(char_one) + value)
            email = email.replace(char_one, new_char)
            print(email)
        else:
            print(email)
            commands = input()
            continue

    elif command == "Validation":
        if len(email) < 6:
            print("Email must be at least 6 characters long!")

        contains_dif = False
        for el in email:
            if not el.isalnum():
                contains_dif = True
            if not el == "@":
                contains_dif = True
        if not contains_dif:
            print("Email must consist only of letters, digits and @!")

        if email.islower():
            print("Email must consist at least one uppercase letter!")

        if email.isupper():
            print("Email must consist at least one lowercase letter!")

        contains_digit = False
        for el in email:
            if el.isdigit():
                contains_digit = True
                commands = input()
                continue
        if not contains_digit:
            print("Email must consist at least one digit!")

    else:
        commands = input()
        continue

    commands = input()
