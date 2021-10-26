player_name = input()

best_player = ""
best_score = 0

while not player_name == "END":
    goals = int(input())
    if goals > best_score:
        best_player = player_name
        best_score = goals
    if goals >= 10:
        break

    player_name = input()

print(f"{best_player} is the best player!")
if best_score >= 3:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score} goals.")