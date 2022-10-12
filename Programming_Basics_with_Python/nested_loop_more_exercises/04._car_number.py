def car_number(start_number, end_number):
    special_numbers = []

    for n1 in range(start_number, end_number + 1):
        for n2 in range(start_number, end_number + 1):
            for n3 in range(start_number, end_number + 1):
                for n4 in range(start_number, end_number + 1):
                    nums_sum = n2 + n3
                    if n1 % 2 == 0 and n4 % 2 == 1 and n1 > n4 and nums_sum % 2 == 0:
                        special_numbers.append(f'{n1}{n2}{n3}{n4}')
                    elif n1 % 2 == 1 and n4 % 2 == 0 and n1 > n4 and nums_sum % 2 == 0:
                        special_numbers.append(f'{n1}{n2}{n3}{n4}')

    return ' '.join(special_numbers)


start_number = int(input())
end_number = int(input())

print(car_number(start_number, end_number))