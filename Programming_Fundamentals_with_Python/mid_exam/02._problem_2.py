<<<<<<< HEAD
username = input().split(", ")
data = input()
blacklist_count = 0
number_of_lost_names = 0

while not data == "Report":
    command = data.split()

    if command[0] == "Blacklist":
        if command[1] in username:
            current_name = command[1]
            username.insert(username.index(command[1]), "Blacklisted")
            username.remove(command[1])
            print(f"{current_name} was blacklisted.")
            blacklist_count += 1
        else:
            print(f"{command[1]} was not found.")

    elif command[0] == "Error":
        command = int(command[1])
        current_name = username[command]
        if command in range(len(username)) and command >= 0 and not current_name == "Blacklisted"  \
                and not current_name == "Lost":
            print(f"{current_name} was lost due to an error.")
            username.insert(command, "Lost")
            username.remove(current_name)
            number_of_lost_names += 1

    elif command[0] == "Change":
        index = int(command[1])
        if index in range(len(username)) and index >= 0:
            current_name = username[index]
            new_name = command[2]
            username.insert(index, new_name)
            username.remove(current_name)
            print(f"{current_name} changed his username to {new_name}.")

    data = input()
print(f"Blacklisted names: {blacklist_count}")
print(f"Lost names: {number_of_lost_names}")
=======
username = input().split(", ")
data = input()
blacklist_count = 0
number_of_lost_names = 0

while not data == "Report":
    command = data.split()

    if command[0] == "Blacklist":
        if command[1] in username:
            current_name = command[1]
            username.insert(username.index(command[1]), "Blacklisted")
            username.remove(command[1])
            print(f"{current_name} was blacklisted.")
            blacklist_count += 1
        else:
            print(f"{command[1]} was not found.")

    elif command[0] == "Error":
        command = int(command[1])
        current_name = username[command]
        if command in range(len(username)) and command >= 0 and not current_name == "Blacklisted"  \
                and not current_name == "Lost":
            print(f"{current_name} was lost due to an error.")
            username.insert(command, "Lost")
            username.remove(current_name)
            number_of_lost_names += 1

    elif command[0] == "Change":
        index = int(command[1])
        if index in range(len(username)) and index >= 0:
            current_name = username[index]
            new_name = command[2]
            username.insert(index, new_name)
            username.remove(current_name)
            print(f"{current_name} changed his username to {new_name}.")

    data = input()
print(f"Blacklisted names: {blacklist_count}")
print(f"Lost names: {number_of_lost_names}")
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
print(" ".join(username))