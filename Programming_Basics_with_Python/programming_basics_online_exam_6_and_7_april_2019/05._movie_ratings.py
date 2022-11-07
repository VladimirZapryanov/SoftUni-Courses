films_numbers = int(input())

all_films_ratings = 0
highest_film_rating = 0
highest_film_name = ''
lowest_film_rating = 10
lowest_film_name = ''

for _ in range(films_numbers):
    film_name = input()
    film_rating = float(input())

    all_films_ratings += film_rating

    if film_rating > highest_film_rating:
        highest_film_rating = film_rating
        highest_film_name = film_name

    if film_rating < lowest_film_rating:
        lowest_film_rating = film_rating
        lowest_film_name = film_name

average_film_rating = all_films_ratings / films_numbers

print(f'{highest_film_name} is with highest rating: {highest_film_rating:.1f}')
print(f'{lowest_film_name} is with lowest rating: {lowest_film_rating:.1f}')
print(f'Average rating: {average_film_rating:.1f}')
