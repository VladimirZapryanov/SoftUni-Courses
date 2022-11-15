number_str = list(input())
number_range = len(number_str)

for _ in range(number_range):
    for n1 in range(number_range):
        if n1 + 1 == number_range:
            break
        first_number = int(number_str[n1])
        second_number = int(number_str[n1 + 1])

        if second_number > first_number:
            number_str[n1], number_str[n1 + 1] = number_str[n1 + 1], number_str[n1]

print(''.join(number_str))