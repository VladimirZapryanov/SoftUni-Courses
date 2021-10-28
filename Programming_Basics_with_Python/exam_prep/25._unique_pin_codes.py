upper_limit_of_first_number = int(input())
upper_limit_of_second_number = int(input())
upper_limit_of_third_number = int(input())

for num_1 in range(1, upper_limit_of_first_number + 1):
    if num_1 % 2 == 0:
        for num_2 in range(1, upper_limit_of_second_number + 1):
            if num_2 % 2 == 1 or num_2 == 2:
                if num_2 // num_2 == 1 and num_2 != 1:
                    for num_3 in range(1, upper_limit_of_third_number + 1):
                        if num_3 % 2 == 0:
                            print(num_1, num_2, num_3)
