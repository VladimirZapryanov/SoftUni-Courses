number_k = int(input())
number_l = int(input())
number_m = int(input())
number_n = int(input())

substitutes_count = 0
for n1 in range(number_k, 9):
    for n2 in range(9, number_l - 1, -1):
        for n3 in range(number_m, 9):
            for n4 in range(9, number_n - 1, -1):
                if n1 % 2 == 0 and n3 % 2 == 0 and n2 % 2 == 1 and n4 % 2 == 1:
                    first_player = f'{n1}{n2}'
                    second_player = f'{n3}{n4}'
                    if first_player == second_player:
                        print('Cannot change the same player.')
                    else:
                        substitutes_count += 1
                        print(f'{first_player} - {second_player}')

                    if substitutes_count == 6:
                        exit()