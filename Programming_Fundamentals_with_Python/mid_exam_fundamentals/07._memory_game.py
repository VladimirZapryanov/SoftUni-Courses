numbers = input().split()
guest_numbers = input()
count = 0
while not guest_numbers == "end":
    count += 1
    data = guest_numbers.split()
    num_1 = int(data[0])
    num_2 = int(data[1])
    if num_1 == num_2 or num_1 not in range(len(numbers)) or num_2 not in range(len(numbers)):
        numbers.insert(int(len(numbers) / 2), f"-{count}a")
        numbers.insert(int(len(numbers) / 2), f"-{count}a")
        print("Invalid input! Adding additional elements to the board")
    elif numbers[num_1] == numbers[num_2]:
        print(f"Congrats! You have found matching elements - {numbers[num_1]}!")
        if num_1 == 0:
            numbers.pop(num_1)
            numbers.pop(num_2 - 1)
        else:
            numbers.pop(num_1)
            numbers.pop(num_2)

    elif numbers[num_1] != numbers[num_2]:
        print("Try again!")

    if len(numbers) == 0:
        print(f"You have won in {count} turns!")
        exit()

    guest_numbers = input()

if len(numbers) > 0:
    print("Sorry you lose :(")

print(" ".join(numbers))