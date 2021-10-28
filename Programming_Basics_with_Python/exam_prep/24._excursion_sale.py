sea_excursion_count = int(input())
mountain_excursion_count = int(input())
command = input()

money = 0

while not command == "Stop":
    destination = command
    if destination == "sea" and sea_excursion_count > 0:
        sea_excursion_count -= 1
        money += 680
    elif destination == "mountain" and mountain_excursion_count > 0:
        mountain_excursion_count -= 1
        money += 499
    elif sea_excursion_count == 0 and mountain_excursion_count == 0:
        break

    command = input()

if sea_excursion_count == 0 and mountain_excursion_count == 0:
    print("Good job! Everything is sold.")

print(f"Profit: {money} leva.")