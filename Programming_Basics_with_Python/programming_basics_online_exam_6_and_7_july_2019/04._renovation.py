from math import ceil

wall_height = int(input())
wall_width = int(input())
windows_and_doors_percent = int(input())
command = input()

all_walls = wall_width * wall_height * 4
all_walls_without_windows_and_doors = ceil(all_walls - (all_walls * windows_and_doors_percent / 100))

while not command == 'Tired!':
    paint_liters = int(command)
    all_walls_without_windows_and_doors -= paint_liters

    if all_walls_without_windows_and_doors <= 0:
        break

    command = input()

if all_walls_without_windows_and_doors > 0:
    print(f'{all_walls_without_windows_and_doors} quadratic m left.')
elif all_walls_without_windows_and_doors < 0:
    print(f'All walls are painted and you have {abs(all_walls_without_windows_and_doors)} l paint left!')
else:
    print(f'All walls are painted! Great job, Pesho!')