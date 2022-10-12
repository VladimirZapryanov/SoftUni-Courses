def lucky_number(number):
    all_numbers = []

    for n1 in range(1, 10):
        for n2 in range(1, 10):
            for n3 in range(1, 10):
                for n4 in range(1, 10):
                    sum1 = n1 + n2
                    sum2 = n3 + n4
                    if sum1 == sum2 and number % sum1 == 0:
                        all_numbers.append(f'{n1}{n2}{n3}{n4}')

    return ' '.join(all_numbers)


number = int(input())

print(lucky_number(number))
