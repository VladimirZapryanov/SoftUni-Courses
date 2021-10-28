tournament_days = int(input())

win_games = 0
lose_games = 0
money = 0
total_money = 0
all_win_games = 0
all_lose_games = 0


for day in range(tournament_days):
    command = input()
    while not command == "Finish":
        sport = command
        score = input()
        if score == "win":
            win_games += 1
            money += 20
        elif score == "lose":
            lose_games += 1
        command = input()

    if win_games > lose_games:
        money += money * 0.1
        all_win_games += 1
    else:
        all_lose_games += 1

    total_money += money
    win_games = 0
    lose_games = 0
    money = 0

if all_win_games > all_lose_games:
    total_money += total_money * 0.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")


