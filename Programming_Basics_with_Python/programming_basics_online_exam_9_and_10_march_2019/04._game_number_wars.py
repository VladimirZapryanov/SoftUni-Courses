first_player_name = input()
second_player_name = input()
command = input()

first_player_points = 0
second_player_points = 0
number_wars = False
first_player_win = False
second_player_win = False
while not command == 'End of game':
    first_player_card = int(command)
    second_player_card = int(input())
    if first_player_card > second_player_card:
        first_player_points += first_player_card - second_player_card
    elif second_player_card > first_player_card:
        second_player_points += second_player_card - first_player_card
    elif first_player_card == second_player_card:
        number_wars = True
        first_player_war_card = int(input())
        second_player_war_card = int(input())
        if first_player_war_card > second_player_war_card:
            first_player_win = True
        elif second_player_war_card > first_player_war_card:
            second_player_win = True
        break

    command = input()

if number_wars:
    print('Number wars!')
    if first_player_win:
        print(f'{first_player_name} is winner with {first_player_points} points')
    elif second_player_win:
        print(f'{second_player_name} is winner with {second_player_points} points')
else:
    print(f'{first_player_name} has {first_player_points} points')
    print(f'{second_player_name} has {second_player_points} points')


