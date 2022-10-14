control_number = int(input())
count = 0
password = ''

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == control_number and a < b and c > d:
                    count += 1
                    if count == 4:
                        password = f'{a}{b}{c}{d}'
                    print(f'{a}{b}{c}{d}', end=' ')

if password:
    print(f'\nPassword: {password}')
else:
    print('\nNo!')
