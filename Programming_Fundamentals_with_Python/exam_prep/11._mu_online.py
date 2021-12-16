dungeons_rooms = input().split("|")
initial_health = 100
initial_bitcoins = 0
rooms = 0
healed_amount = 0
is_you_alive = True

for room in dungeons_rooms:
    command, number = room.split()
    number = int(number)
    rooms += 1

    if command == "potion":
        current_health = initial_health
        initial_health += number
        if initial_health > 100:
            healed_amount = 100 - current_health
            initial_health = 100
        else:
            healed_amount = number
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms}")
            is_you_alive = False
            break

if is_you_alive:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")