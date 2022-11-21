animals = input().split(', ')
animals_count = len(animals)

if animals[animals_count - 1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    wolf_index = animals.index('wolf')
    sheep_number = animals_count - wolf_index - 1
    print(f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!')
