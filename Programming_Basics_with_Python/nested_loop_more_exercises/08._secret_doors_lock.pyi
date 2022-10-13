end_of_first_number = int(input())
end_of_second_number = int(input())
end_of_third_number = int(input())

for num1 in range(1, end_of_first_number + 1):
    for num2 in range(1, end_of_second_number + 1):
        for num3 in range(1, end_of_third_number + 1):
            if num1 % 2 == 0 and num3 % 2 == 0:
                counter = 0
                for nn in range(1, num2 + 1):
                    if num2 % nn == 0:
                        counter += 1
                if counter == 2:
                    print(f'{num1} {num2} {num3}')