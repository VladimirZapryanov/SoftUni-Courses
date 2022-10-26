win_games = 0
lost_games = 0
draw_games = 0
numbers_of_games = 3

for g in range(numbers_of_games):
    score = input()
    if score[0] > score[2]:
        win_games += 1
    elif score[0] < score[2]:
        lost_games += 1
    else:
        draw_games += 1

print(f"Team won {win_games} games.")
print(f"Team lost {lost_games} games.")
print(f"Drawn games: {draw_games}")
