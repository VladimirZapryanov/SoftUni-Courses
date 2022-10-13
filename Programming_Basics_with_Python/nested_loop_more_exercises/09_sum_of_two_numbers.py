def find_combination(start_number, end_number, magic_number):
    first_number = 0
    second_number = 0
    combination_number = 0
    combination = False

    for n1 in range(start_number, end_number + 1):
        if combination:
            break
        for n2 in range(start_number, end_number + 1):
            combination_number += 1
            if n1 + n2 == magic_number:
                combination = True
                first_number = n1
                second_number = n2
                break

    if combination:
        return f'Combination N:{combination_number} ({first_number} + {second_number} = {magic_number})'
    else:
        return f'{combination_number} combinations - neither equals {magic_number}'


start_number = int(input())
end_number = int(input())
magic_number = int(input())

print(find_combination(start_number, end_number, magic_number))