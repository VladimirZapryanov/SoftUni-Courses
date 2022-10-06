bottle_with_detergent = int(input())
command = input()

bottle_value = 750
soap_for_one_plate = 5
soap_for_one_pot = 15
machine_count = 0
clean_pots_count = 0
clean_plates_count = 0

all_soap = bottle_with_detergent * bottle_value

while not command == 'End':
    dishes_for_wash = int(command)
    machine_count += 1

    if machine_count % 3 == 0:
        all_soap -= dishes_for_wash* soap_for_one_pot
        clean_pots_count += dishes_for_wash
    else:
        all_soap -= dishes_for_wash * soap_for_one_plate
        clean_plates_count += dishes_for_wash

    if all_soap < 0:
        break

    command = input()

if all_soap >= 0:
    print('Detergent was enough!')
    print(f'{clean_plates_count} dishes and {clean_pots_count} pots were washed.')
    print(f'Leftover detergent {all_soap} ml.')
else:
    print(f'Not enough detergent, {abs(all_soap)} ml. more necessary!')
