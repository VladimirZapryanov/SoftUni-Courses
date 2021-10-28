money = float(input())
gender = input()
age = int(input())
sport = input()

needed_money = 0

if gender == "m":
    if sport == "Gym":
        needed_money += 42
    elif sport == "Boxing":
        needed_money += 41
    elif sport == "Yoga":
        needed_money += 45
    elif sport == "Zumba":
        needed_money += 34
    elif sport == "Dances":
        needed_money += 51
    elif sport == "Pilates":
        needed_money += 39

elif gender == "f":
    if sport == "Gym":
        needed_money += 35
    elif sport == "Boxing":
        needed_money += 37
    elif sport == "Yoga":
        needed_money += 42
    elif sport == "Zumba":
        needed_money += 31
    elif sport == "Dances":
        needed_money += 53
    elif sport == "Pilates":
        needed_money += 37

final_cost = needed_money

if age <= 19:
    final_cost -= needed_money * 0.2

if money >= final_cost:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(money - final_cost):.2f} more.")

