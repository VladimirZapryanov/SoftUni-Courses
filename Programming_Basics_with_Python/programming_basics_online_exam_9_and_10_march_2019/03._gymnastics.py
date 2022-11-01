country = input()
type_of_exercise = input()

total_score = 0
if country == 'Russia':
    if type_of_exercise == 'ribbon':
        total_score = 9.100 + 9.400
    elif type_of_exercise == 'hoop':
        total_score = 9.300 + 9.800
    elif type_of_exercise == 'rope':
        total_score = 9.600 + 9.000
elif country == 'Bulgaria':
    if type_of_exercise == 'ribbon':
        total_score = 9.600 + 9.400
    elif type_of_exercise == 'hoop':
        total_score = 9.550 + 9.750
    elif type_of_exercise == 'rope':
        total_score = 9.500 + 9.400
elif country == 'Italy':
    if type_of_exercise == 'ribbon':
        total_score = 9.200 + 9.500
    elif type_of_exercise == 'hoop':
        total_score = 9.450 + 9.350
    elif type_of_exercise == 'rope':
        total_score = 9.700 + 9.150

percent = total_score / 20 * 100
not_reached_percent = 100 - percent
print(f'The team of {country} get {total_score:.3f} on {type_of_exercise}.')
print(f'{not_reached_percent:.2f}%')