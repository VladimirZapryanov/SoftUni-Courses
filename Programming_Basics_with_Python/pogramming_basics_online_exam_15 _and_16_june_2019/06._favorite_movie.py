command = input()

limit = 7
best_movie = ''
best_points = 0
while not command == 'STOP':
    current_movie = command
    current_points = 0
    limit -= 1

    for l in range(len(current_movie)):
        if current_movie[l].isupper():
            current_points += ord(current_movie[l]) - len(current_movie)
        elif current_movie[l].islower():
            current_points += ord(current_movie[l]) - (len(current_movie) * 2)
        else:
            current_points += ord(current_movie[l])

    if current_points > best_points:
        best_points = current_points
        best_movie = current_movie

    if limit == 0:
        break

    command = input()

if limit == 0:
    print('The limit is reached.')

print(f'The best movie for you is {best_movie} with {best_points} ASCII sum.')
