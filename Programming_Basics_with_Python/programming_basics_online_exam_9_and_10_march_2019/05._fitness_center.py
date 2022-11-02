people_in_fitness = int(input())

back = 0
chest = 0
legs = 0
belly = 0
protein_shake = 0
protein_bar = 0
training_people = 0
snacks_people = 0
for _ in range(people_in_fitness):
    body_part = input()

    if body_part == 'Back':
        back += 1
        training_people += 1
    elif body_part == 'Chest':
        chest += 1
        training_people += 1
    elif body_part == 'Legs':
        legs += 1
        training_people += 1
    elif body_part == 'Abs':
        belly += 1
        training_people += 1
    elif body_part == 'Protein shake':
        protein_shake += 1
        snacks_people += 1
    elif body_part == 'Protein bar':
        protein_bar += 1
        snacks_people += 1

percent_work_out_people = training_people / people_in_fitness * 100
percent_snacks_people = snacks_people / people_in_fitness * 100

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{belly} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{percent_work_out_people:.2f}% - work out')
print(f'{percent_snacks_people:.2f}% - protein')

