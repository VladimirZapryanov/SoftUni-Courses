number = int(input())

for n in range(1, number + 1):
    print(' ' * (number - n) + '* ' * n)
for n1 in range(number - 1, 0, -1):
    print(' ' * (number - n1) + '* ' * n1)