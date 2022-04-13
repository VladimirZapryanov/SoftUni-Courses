<<<<<<< HEAD
message = input()
data = input()

while not data == "Reveal":
    data = data.split(":|:")

    if data[0] == "InsertSpace":
        left_part = message[:int(data[1])]
        right_part = message[int(data[1]):]
        message = left_part + " " + right_part
        print(message)

    elif data[0] == "Reverse":
        if data[1] in message:
            text = data[1]
            reversed_text = text[::-1]
            message = message.replace(data[1], "", 1) + reversed_text
            print(message)
        else:
            print("error")

    elif data[0] == "ChangeAll":
        while data[1] in message:
            message = message.replace(data[1], data[2])
            print(message)
    data = input()

=======
message = input()
data = input()

while not data == "Reveal":
    data = data.split(":|:")

    if data[0] == "InsertSpace":
        left_part = message[:int(data[1])]
        right_part = message[int(data[1]):]
        message = left_part + " " + right_part
        print(message)

    elif data[0] == "Reverse":
        if data[1] in message:
            text = data[1]
            reversed_text = text[::-1]
            message = message.replace(data[1], "", 1) + reversed_text
            print(message)
        else:
            print("error")

    elif data[0] == "ChangeAll":
        while data[1] in message:
            message = message.replace(data[1], data[2])
            print(message)
    data = input()

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
print(f"You have a new text message: {message}")