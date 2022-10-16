from math import floor

number = int(input())

print('*' * (2 * number) + ' ' * number + '*' * (2 * number))

for n in range(0, number - 2):
    row = floor((number - 1) / 2 - 1)
    if n == row:
        print('*' + '/' * ((2 * number) - 2) + '*' + '|' * number + '*' + '/' * ((2 * number) - 2) + '*')
    else:
        print('*' + '/' * ((2 * number) - 2) + '*' + ' ' * number + '*' + '/' * ((2 * number) - 2) + '*')

print('*' * (2 * number) + ' ' * number + '*' * (2 * number))
