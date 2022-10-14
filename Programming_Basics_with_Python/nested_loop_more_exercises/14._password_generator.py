def password_generator(number_n, number_l):
    passwords = []
    for n1 in range(1, number_n + 1):
        for n2 in range(1, number_n + 1):
            for l1 in range(97, number_l + 97):
                for l2 in range(97, number_l + 97):
                    for n3 in range(1, number_n + 1):
                        first_letter = chr(l1)
                        second_letter = chr(l2)
                        if n3 > n1 and n3 > n2:
                            passwords.append(f'{n1}{n2}{first_letter}{second_letter}{n3}')

    return ' '.join(passwords)


number_n = int(input())
number_l = int(input())

print(password_generator(number_n, number_l))