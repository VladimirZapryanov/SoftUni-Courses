command = input()

sorted_successfully = True
while not command == 'Welcome!':
    name = command
    name_chars = len(name)

    if name == 'Voldemort':
        print('You must not speak of that name!')
        sorted_successfully = False
        break

    if name_chars < 5:
        print(f'{name} goes to Gryffindor.')
    elif name_chars == 5:
        print(f'{name} goes to Slytherin.')
    elif name_chars == 6:
        print(f'{name} goes to Ravenclaw.')
    else:
        print(f'{name} goes to Hufflepuff.')

    command = input()

if sorted_successfully:
    print('Welcome to Hogwarts.')