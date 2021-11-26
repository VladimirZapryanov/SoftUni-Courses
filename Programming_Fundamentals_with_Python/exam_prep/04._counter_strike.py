energy = int(input())
command = input()

won_counter = 0
is_it_won = True

while not command == "End of battle":
    distance = int(command)
    if energy - distance >= 0:
        won_counter += 1
        energy -= distance
        if won_counter % 3 == 0:
            energy += won_counter
    else:
        print(f"Not enough energy! Game ends with {won_counter} won battles and {energy} energy")
        is_it_won = False
        break
    command = input()

if is_it_won:
    print(f"Won battles: {won_counter}. Energy left: {energy}")