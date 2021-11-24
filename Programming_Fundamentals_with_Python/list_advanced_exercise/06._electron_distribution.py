first_number = int(input())
number_of_electrons = first_number

shells = []

for n in range(1, first_number + 1):
    if number_of_electrons > 0:
        number = 2 * pow(n, 2)
        if number < number_of_electrons:
            shells.append(number)
            number_of_electrons -= number
        if number > number_of_electrons and not number_of_electrons == 0:
            shells.append(number_of_electrons)
            break

print(shells)
