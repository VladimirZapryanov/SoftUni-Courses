def painting_eggs(egg_size, egg_colour, eggs_numbers, large, medium, small):
    price = 0
    if egg_size == 'Large':
        if egg_colour == 'Red':
            price = eggs_numbers * large['red']
        elif egg_colour == 'Green':
            price = eggs_numbers * large['green']
        elif egg_colour == 'Yellow':
            price = eggs_numbers * large['yellow']
    elif egg_size == 'Medium':
        if egg_colour == 'Red':
            price = eggs_numbers * medium['red']
        elif egg_colour == 'Green':
            price = eggs_numbers * medium['green']
        elif egg_colour == 'Yellow':
            price = eggs_numbers * medium['yellow']
    elif egg_size == 'Small':
        if egg_colour == 'Red':
            price = eggs_numbers * small['red']
        elif egg_colour == 'Green':
            price = eggs_numbers * small['green']
        elif egg_colour == 'Yellow':
            price = eggs_numbers * small['yellow']

    final_price = price * 0.65
    return f'{final_price:.2f} leva.'


egg_size = input()
egg_colour = input()
eggs_numbers = int(input())

large = {
    'red': 16,
    'green': 12,
    'yellow': 9,
}

medium = {
    'red': 13,
    'green': 9,
    'yellow': 7,
}

small = {
    'red': 9,
    'green': 8,
    'yellow': 5,
}

print(painting_eggs(egg_size, egg_colour, eggs_numbers, large, medium, small))