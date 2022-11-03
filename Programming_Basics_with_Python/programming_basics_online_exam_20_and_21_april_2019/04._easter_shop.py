starting_amount_of_eggs = int(input())
command = input()

sold_eggs = 0
not_enough_eggs = False
while not command == 'Close':
    eggs_numbers = int(input())

    if command == 'Fill':
        starting_amount_of_eggs += eggs_numbers
    elif command == 'Buy':
        if starting_amount_of_eggs >= eggs_numbers:
            sold_eggs += eggs_numbers
            starting_amount_of_eggs -= eggs_numbers
        else:
            not_enough_eggs = True
            break

    command = input()

if not_enough_eggs:
    print('Not enough eggs in store!')
    print(f'You can buy only {starting_amount_of_eggs}.')
else:
    print('Store is closed!')
    print(f'{sold_eggs} eggs sold.')