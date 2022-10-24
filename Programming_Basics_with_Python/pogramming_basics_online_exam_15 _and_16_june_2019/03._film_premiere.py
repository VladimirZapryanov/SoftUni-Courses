movie_name = input()
type_of_package = input()
tickets_numbers = int(input())

tickets_price = 0
if movie_name == 'John Wick':
    if type_of_package == 'Drink':
        tickets_price = tickets_numbers * 12
    elif type_of_package == 'Popcorn':
        tickets_price = tickets_numbers * 15
    elif type_of_package == 'Menu':
        tickets_price = tickets_numbers * 19
elif movie_name == 'Star Wars':
    if type_of_package == 'Drink':
        tickets_price = tickets_numbers * 18
    elif type_of_package == 'Popcorn':
        tickets_price = tickets_numbers * 25
    elif type_of_package == 'Menu':
        tickets_price = tickets_numbers * 30

    if tickets_numbers >= 4:
        tickets_price = tickets_price* 0.70
elif movie_name == 'Jumanji':
    if type_of_package == 'Drink':
        tickets_price = tickets_numbers * 9
    elif type_of_package == 'Popcorn':
        tickets_price = tickets_numbers * 11
    elif type_of_package == 'Menu':
        tickets_price = tickets_numbers * 14

    if tickets_numbers == 2:
        tickets_price = tickets_price * 0.85

print(f'Your bill is {tickets_price:.2f} leva.')
