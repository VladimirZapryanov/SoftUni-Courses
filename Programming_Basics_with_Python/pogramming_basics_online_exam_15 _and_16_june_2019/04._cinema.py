cinema_capacity = int(input())
command = input()

ticket_price = 5
profit = 0
while not command == 'Movie time!':
    people = int(command)
    cinema_capacity -= people
    if cinema_capacity < 0:
        break

    if people % 3 == 0:
        profit += ticket_price * people - 5
    else:
        profit += ticket_price * people

    command = input()

if cinema_capacity >= 0:
    print(f'There are {cinema_capacity} seats left in the cinema.')
else:
    print('The cinema is full.')

print(f'Cinema income - {profit} lv.')