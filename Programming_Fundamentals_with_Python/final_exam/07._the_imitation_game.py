encrypted_message = input()
commands = input()

while not commands == "Decode":
    data = commands.split("|")
    command = data[0]
    if command == "Move":
        moved_part = encrypted_message[:int(data[1])]
        encrypted_message = encrypted_message.replace(moved_part, "") + moved_part
    elif command == "Insert":
        left_part = encrypted_message[:int(data[1])]
        right_part = encrypted_message[int(data[1]):]
        encrypted_message = left_part + data[2] + right_part
    elif command == "ChangeAll":
        encrypted_message = encrypted_message.replace(data[1], data[2])

    commands = input()

print(f"The decrypted message is: {encrypted_message}")