first_number = int(input())
sec_number = int(input())

for number in range(first_number, sec_number + 1):
    sum_of_odd_position = 0
    sum_of_even_position = 0
    for index, value in enumerate(str(number)):
        value = int(value)
        if (index + 1) % 2 == 0:
            sum_of_even_position += value
        else:
            sum_of_odd_position += value
    if sum_of_odd_position == sum_of_even_position:
        print(number, end=' ')
