from math import floor

numbers_of_tournaments = int(input())
initial_points = int(input())

won_point = 0
won_games = 0
w = 2000
f = 1200
sf = 720
for t in range(numbers_of_tournaments):
    tournament_stage = input()
    if tournament_stage == 'W':
        won_point += w
        won_games += 1
    elif tournament_stage == 'F':
        won_point += f
    elif tournament_stage == 'SF':
        won_point += sf

final_points = won_point + initial_points
average_points = floor(won_point / numbers_of_tournaments)
percent_won_games = won_games / numbers_of_tournaments * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{percent_won_games:.2f}%')