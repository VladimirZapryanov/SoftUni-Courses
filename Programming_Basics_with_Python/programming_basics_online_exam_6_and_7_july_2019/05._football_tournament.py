team_name = input()
matches = int(input())

total_score = 0
win_matches = 0
draw_matches = 0
lost_matches = 0

for m in range(matches):
    result = input()
    if result == 'W':
        total_score += 3
        win_matches += 1
    elif result == 'D':
        total_score += 1
        draw_matches += 1
    elif result == 'L':
        lost_matches += 1

if matches == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    percent_win_games = win_matches / matches * 100
    print(f'{team_name} has won {total_score} points during this season.')
    print('Total stats:')
    print(f'## W: {win_matches}')
    print(f'## D: {draw_matches}')
    print(f'## L: {lost_matches}')
    print(f'Win rate: {percent_win_games:.2f}%')