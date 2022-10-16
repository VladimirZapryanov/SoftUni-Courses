n = int(input())
roof = int((n + 1) / 2)

for r in range(1, roof + 1):
    if n % 2 == 1:
        if r == 1:
            print('-' * (roof - 1) + '*' + '-' * (roof - 1))
        else:
            print('-' * (roof - r) + '*' + '**' * (r - 1) + '-' * (roof - r))
    else:
        if r == 1:
            print('-' * (roof - 1) + '**' + '-' * (roof - 1))
        else:
            print('-' * (roof - r) + '**' + '**' * (r - 1) + '-' * (roof - r))

house = n - roof
for h in range(1, house + 1):
    print('|' + '*' * (n - 2) + '|')