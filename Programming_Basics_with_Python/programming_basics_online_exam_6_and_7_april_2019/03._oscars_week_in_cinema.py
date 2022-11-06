def cinema_income(film_name, type_of_room, tickets_count, a_star_is_born, bohemian_rhapsody, green_book, the_favourite):
    total_income = 0
    if film_name == 'A Star Is Born':
        if type_of_room == 'normal':
            total_income = tickets_count * a_star_is_born['normal']
        elif type_of_room == 'luxury':
            total_income = tickets_count * a_star_is_born['luxury']
        elif type_of_room == 'ultra luxury':
            total_income = tickets_count * a_star_is_born['ultra luxury']
    elif film_name == 'Bohemian Rhapsody':
        if type_of_room == 'normal':
            total_income = tickets_count * bohemian_rhapsody['normal']
        elif type_of_room == 'luxury':
            total_income = tickets_count * bohemian_rhapsody['luxury']
        elif type_of_room == 'ultra luxury':
            total_income = tickets_count * bohemian_rhapsody['ultra luxury']
    elif film_name == 'Green Book':
        if type_of_room == 'normal':
            total_income = tickets_count * green_book['normal']
        elif type_of_room == 'luxury':
            total_income = tickets_count * green_book['luxury']
        elif type_of_room == 'ultra luxury':
            total_income = tickets_count * green_book['ultra luxury']
    elif film_name == 'The Favourite':
        if type_of_room == 'normal':
            total_income = tickets_count * the_favourite['normal']
        elif type_of_room == 'luxury':
            total_income = tickets_count * the_favourite['luxury']
        elif type_of_room == 'ultra luxury':
            total_income = tickets_count * the_favourite['ultra luxury']

    return total_income


film_name = input()
type_of_room = input()
tickets_count = int(input())

a_star_is_born = {
    'normal': 7.50,
    'luxury': 10.50,
    'ultra luxury': 13.50,
}

bohemian_rhapsody = {
    'normal': 7.35,
    'luxury': 9.45,
    'ultra luxury': 12.75,
}

green_book = {
    'normal': 8.15,
    'luxury': 10.25,
    'ultra luxury': 13.25,
}

the_favourite = {
    'normal': 8.75,
    'luxury': 11.55,
    'ultra luxury': 13.95,
}

print(f'{film_name} -> {cinema_income(film_name, type_of_room, tickets_count, a_star_is_born, bohemian_rhapsody, green_book, the_favourite):.2f} lv.')