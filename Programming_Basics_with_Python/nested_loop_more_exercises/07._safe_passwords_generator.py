first_number = int(input())
second_number = int(input())
max_passwords = int(input())
a = 34
b = 63

for x in range(1, first_number + 1):
    for y in range(1, second_number + 1):
        a += 1
        b += 1
        if a > 55:
            a = 35
        if b > 96:
            b = 64
        if max_passwords <= 0:
            break
        max_passwords -= 1
        print(f'{chr(a)}{chr(b)}{x}{y}{chr(b)}{chr(a)}', end='|')

