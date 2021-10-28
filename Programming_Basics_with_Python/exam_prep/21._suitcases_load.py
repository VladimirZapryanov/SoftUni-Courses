capacity_airplane = float(input())
command = input()

taken_space = 0
suitcase_counter = 0
no_more_space = False

while not command == 'End':
    volume_suitcase = float(command)
    taken_space += volume_suitcase
    if taken_space >= capacity_airplane:
        no_more_space = True
        break
    suitcase_counter += 1
    if suitcase_counter % 3 == 0:
        volume_suitcase += 0.1 * volume_suitcase
    command = input()

if no_more_space:
    print(f"No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcase_counter} suitcases loaded.")
