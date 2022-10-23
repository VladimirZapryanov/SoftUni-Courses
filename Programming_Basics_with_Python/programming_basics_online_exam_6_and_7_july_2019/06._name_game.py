command = input()

win_player_name = ''
win_player_score = 0

while not command == 'Stop':
    current_name = command
    current_score = 0
    n = len(current_name)

    for x in range(n):
        number = int(input())
        if number == ord(current_name[x]):
            current_score += 10
        else:
            current_score += 2

        if current_score >= win_player_score:
            win_player_name = current_name
            win_player_score = current_score

    command = input()

print(f'The winner is {win_player_name} with {win_player_score} points!')