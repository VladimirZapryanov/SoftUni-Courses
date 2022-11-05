easter_bread_count = int(input())

the_best_baker_name = ''
the_best_baker_score = 0
for _ in range(easter_bread_count):
    baker_name = input()
    command = input()
    total_baker_score = 0
    while not command == 'Stop':
        baker_score = int(command)
        total_baker_score += baker_score

        command = input()

    print(f'{baker_name} has {total_baker_score} points.')
    if total_baker_score > the_best_baker_score:
        the_best_baker_score = total_baker_score
        the_best_baker_name = baker_name
        print(f'{baker_name} is the new number 1!')

print(f'{the_best_baker_name} won competition with {the_best_baker_score} points!')