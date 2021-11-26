targets = [int(el) for el in input().split()]
string = input()

while not string == "End":
    command, index, power = string.split()
    index = int(index)
    power = int(power)

    if index not in range(len(targets)) and command == "Add":
        print("Invalid placement!")
        string = input()
        continue

    if command == "Shoot":
        targets[index] -= power
        if targets[index] <= 0:
            targets.remove(targets[index])

    elif command == "Add":
        targets[index] += power

    elif command == "Strike":
        left_most_index = index - power
        right_most_index = index + power
        if left_most_index in range(len(targets)) and right_most_index in range(len(targets)):
            left_unstriked_part = targets[:left_most_index]
            right_unstrike_part = targets[right_most_index+1:]
            targets = left_unstriked_part + right_unstrike_part
        else:
            print("Strike missed!")

    string = input()

print("|".join(str(el) for el in targets))
