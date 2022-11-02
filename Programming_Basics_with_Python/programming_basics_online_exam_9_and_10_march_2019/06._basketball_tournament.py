command = input()

all_games_count = 0
lost_games_count = 0
win_games_count = 0
while not command == 'End of tournaments':
    tournament_name = command
    games_numbers = int(input())
    all_games_count += games_numbers

    for g in range(1, games_numbers + 1):
        dessy_team_points = int(input())
        other_team_points = int(input())

        points_difference = dessy_team_points - other_team_points
        if dessy_team_points > other_team_points:
            win_games_count += 1
            print(f'Game {g} of tournament {tournament_name}: win with {points_difference} points.')
        elif dessy_team_points < other_team_points:
            lost_games_count += 1
            print(f'Game {g} of tournament {tournament_name}: lost with {abs(points_difference)} points.')

    command = input()

lost_games_percent = lost_games_count / all_games_count * 100
win_games_percent = win_games_count / all_games_count * 100
print(f'{win_games_percent:.2f}% matches win')
print(f'{lost_games_percent:.2f}% matches lost')


