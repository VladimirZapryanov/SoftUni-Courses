from collections import deque

quantity_of_water = int(input())
qq = deque()

name = input()

while not name == "Start":
    qq.append(name)
    name = input()

command = input()

while not command == "End":
    command = command.split()
    if command[0] == "refill":
        quantity_of_water += int(command[1])
    else:
        quantity_of_water -= int(command[0])

        if quantity_of_water >= 0:
            print(f"{qq.popleft()} got water")
        else:
            print(f"{qq.popleft()} must wait")
            quantity_of_water += int(command[0])

    command = input()

print(f"{quantity_of_water} liters left")