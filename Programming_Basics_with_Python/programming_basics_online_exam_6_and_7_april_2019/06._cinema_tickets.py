command = input()

all_tickets_count = 0
all_student_tickets_count = 0
all_standard_tickets_count = 0
all_kid_tickets_count = 0

while not command == 'Finish':
    film_name = command
    free_room_seats = int(input())

    current_film_tickets_count = 0
    current_film_student_tickets_count = 0
    current_film_standard_tickets_count = 0
    current_film_kid_tickets_count = 0

    new_command = input()
    while not new_command == 'End':
        tickets_type = new_command
        current_film_tickets_count += 1
        all_tickets_count += 1
        if tickets_type == 'student':
            current_film_student_tickets_count += 1
            all_student_tickets_count += 1
        elif tickets_type == 'standard':
            current_film_standard_tickets_count += 1
            all_standard_tickets_count += 1
        elif tickets_type == 'kid':
            current_film_kid_tickets_count += 1
            all_kid_tickets_count += 1

        if current_film_tickets_count == free_room_seats:
            break
        else:
            new_command = input()

    sold_tickets_percent = current_film_tickets_count / free_room_seats * 100
    print(f'{film_name} - {sold_tickets_percent:.2f}% full.')

    command = input()

student_tickets_percent = all_student_tickets_count / all_tickets_count * 100
standard_tickets_percent = all_standard_tickets_count / all_tickets_count * 100
kid_tickets_percent = all_kid_tickets_count / all_tickets_count * 100

print(f'Total tickets: {all_tickets_count}')
print(f'{student_tickets_percent:.2f}% student tickets.')
print(f'{standard_tickets_percent:.2f}% standard tickets.')
print(f'{kid_tickets_percent:.2f}% kids tickets.')