painted_eggs_count = int(input())

red_eggs_count = 0
orange_eggs_count = 0
blue_eggs_count = 0
green_eggs_count = 0
for _ in range(painted_eggs_count):
    egg_colour = input()
    if egg_colour == 'red':
        red_eggs_count += 1
    elif egg_colour == 'orange':
        orange_eggs_count += 1
    elif egg_colour == 'green':
        green_eggs_count += 1
    elif egg_colour == 'blue':
        blue_eggs_count += 1

max_eggs_count = max(red_eggs_count, orange_eggs_count, blue_eggs_count, green_eggs_count)
max_eggs_colour = ''
if max_eggs_count == red_eggs_count:
    max_eggs_colour = 'red'
elif max_eggs_count == orange_eggs_count:
    max_eggs_colour = 'orange'
elif max_eggs_count == blue_eggs_count:
    max_eggs_colour = 'blue'
elif max_eggs_count == green_eggs_count:
    max_eggs_colour = 'green'

print(f'Red eggs: {red_eggs_count}')
print(f'Orange eggs: {orange_eggs_count}')
print(f'Blue eggs: {blue_eggs_count}')
print(f'Green eggs: {green_eggs_count}')
print(f'Max eggs: {max_eggs_count} -> {max_eggs_colour}')