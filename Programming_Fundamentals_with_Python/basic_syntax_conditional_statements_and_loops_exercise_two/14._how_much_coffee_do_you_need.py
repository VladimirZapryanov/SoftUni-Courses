command = input()

list_of_works = ['coding',
                 'CODING',
                 'dog',
                 'DOG',
                 'cat',
                 'CAT',
                 'movie',
                 'MOVIE'
                 ]
needed_coffee_count = 0
max_coffee_before_sleep = 5
while not command == 'END':
    work = command
    if work not in list_of_works:
        command = input()
        continue

    if work.islower():
        needed_coffee_count += 1
    elif work.isupper():
        needed_coffee_count += 2

    command = input()

if needed_coffee_count <= max_coffee_before_sleep:
    print(needed_coffee_count)
else:
    print('You need extra sleep')
