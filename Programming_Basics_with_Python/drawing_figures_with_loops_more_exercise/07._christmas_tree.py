number = int(input())

for n in range(1, number + 1):
    first_spaces = number + 1
    second_spaces = number - n
    if n <= 1:
        print(' ' * first_spaces + '|')
        print(' ' * second_spaces + '*' * n + ' ' + '|' + ' ' + '*' * n)
    else:
        print(' ' * second_spaces + '*' * n + ' ' + '|' + ' ' + '*' * n)

