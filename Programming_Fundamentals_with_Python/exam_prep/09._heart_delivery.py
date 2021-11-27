neighborhood = [int(num) for num in input().split("@")]

command = input()
position = 0

while not command == "Love!":
    length_jump = command.split()[1]
    length_jump = int(length_jump)

    position = position + length_jump

    if position >= len(neighborhood):
        position = 0

    if neighborhood[position] == 0:
        print(f"Place {position} already had "
              f"Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {position}.")

counter = 0
for num in neighborhood:
    if not num == 0:
        counter += 1

if counter == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")