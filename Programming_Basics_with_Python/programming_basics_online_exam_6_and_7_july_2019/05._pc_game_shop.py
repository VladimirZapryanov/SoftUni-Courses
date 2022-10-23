sell_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for n in range(0, sell_games):
    game_name = input()

    if game_name == 'Hearthstone':
        hearthstone += 1
    elif game_name == 'Fornite':
        fornite += 1
    elif game_name == 'Overwatch':
        overwatch += 1
    else:
        others += 1

hearthstone_percent = hearthstone / sell_games * 100
fornite_percent = fornite / sell_games * 100
overwatch_percent = overwatch / sell_games * 100
others_percent = others / sell_games * 100

print(f'Hearthstone - {hearthstone_percent:.2f}%')
print(f'Fornite - {fornite_percent:.2f}%')
print(f'Overwatch - {overwatch_percent:.2f}%')
print(f'Others - {others_percent:.2f}%')