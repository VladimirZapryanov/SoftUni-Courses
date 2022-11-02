player_name = input()
command = input()

total_points = 301
successful_shots = 0
failed_shots = 0
while not command == 'Retire':
    section = command
    points = int(input())

    current_point = 0
    if section == 'Single':
        current_point = points
    elif section == 'Double':
        current_point = points * 2
    elif section == 'Triple':
        current_point = points * 3

    if total_points >= current_point:
        total_points -= current_point
        successful_shots += 1
    else:
        failed_shots += 1

    if total_points == 0:
        break

    command = input()

if total_points == 0:
    print(f'{player_name} won the leg with {successful_shots} shots.')
else:
    print(f'{player_name} retired after {failed_shots} unsuccessful shots.')