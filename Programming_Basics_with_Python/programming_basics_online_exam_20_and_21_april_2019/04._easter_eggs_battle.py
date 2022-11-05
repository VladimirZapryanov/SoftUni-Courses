first_player_eggs_count = int(input())
second_player_eggs_count = int(input())
command = input()

message = ''
no_winner = True
while not command == 'End':
    winner = command
    if winner == 'one':
        second_player_eggs_count -= 1
        if second_player_eggs_count == 0:
            no_winner = False
            message = f'Player two is out of eggs. Player one has {first_player_eggs_count} eggs left.'
            break
    elif winner == 'two':
        first_player_eggs_count -= 1
        if first_player_eggs_count == 0:
            no_winner = False
            message = f'Player one is out of eggs. Player two has {second_player_eggs_count} eggs left.'
            break

    command = input()

if no_winner:
    print(f'Player one has {first_player_eggs_count} eggs left.')
    print(f'Player two has {second_player_eggs_count} eggs left.')
else:
    print(message)