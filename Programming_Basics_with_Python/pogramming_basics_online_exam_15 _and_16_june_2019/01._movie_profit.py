movie_name = input()
days = int(input())
tickets_number = int(input())
ticket_price = float(input())
percent_for_cinema = int(input())

movie_profit = days * tickets_number * ticket_price
cinema_profit = movie_profit * percent_for_cinema / 100
total_profit = movie_profit - cinema_profit

print(f'The profit from the movie {movie_name} is {total_profit:.2f} lv.')