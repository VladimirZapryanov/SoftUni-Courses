team_name = input()
type_of_souvenir = input()
souvenirs_numbers = int(input())

team_list = ['Argentina', 'Brazil', 'Croatia', 'Denmark']
souvenirs_list = ['flags', 'caps', 'posters', 'stickers']

total_price = 0

if team_name == 'Argentina':
    if type_of_souvenir == 'flags':
        total_price = souvenirs_numbers * 3.25
    elif type_of_souvenir == 'caps':
        total_price = souvenirs_numbers * 7.20
    elif type_of_souvenir == 'posters':
        total_price = souvenirs_numbers * 5.10
    elif type_of_souvenir == 'stickers':
        total_price = souvenirs_numbers * 1.25
elif team_name == 'Brazil':
    if type_of_souvenir == 'flags':
        total_price = souvenirs_numbers * 4.20
    elif type_of_souvenir == 'caps':
        total_price = souvenirs_numbers * 8.50
    elif type_of_souvenir == 'posters':
        total_price = souvenirs_numbers * 5.35
    elif type_of_souvenir == 'stickers':
        total_price = souvenirs_numbers * 1.20
elif team_name == 'Croatia':
    if type_of_souvenir == 'flags':
        total_price = souvenirs_numbers * 2.75
    elif type_of_souvenir == 'caps':
        total_price = souvenirs_numbers * 6.90
    elif type_of_souvenir == 'posters':
        total_price = souvenirs_numbers * 4.95
    elif type_of_souvenir == 'stickers':
        total_price = souvenirs_numbers * 1.10
elif team_name == 'Denmark':
    if type_of_souvenir == 'flags':
        total_price = souvenirs_numbers * 3.10
    elif type_of_souvenir == 'caps':
        total_price = souvenirs_numbers * 6.50
    elif type_of_souvenir == 'posters':
        total_price = souvenirs_numbers * 4.80
    elif type_of_souvenir == 'stickers':
        total_price = souvenirs_numbers * 0.90

if team_name in team_list and type_of_souvenir in souvenirs_list:
    print(f'Pepi bought {souvenirs_numbers} {type_of_souvenir} of {team_name} for {total_price:.2f} lv.')

if team_name not in team_list:
    print('Invalid country!')

if type_of_souvenir not in souvenirs_list:
    print('Invalid stock!')