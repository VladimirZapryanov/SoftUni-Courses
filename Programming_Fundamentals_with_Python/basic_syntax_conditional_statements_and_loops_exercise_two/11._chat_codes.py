numbers_of_rows = int(input())

for _ in range(numbers_of_rows):
    code_number = int(input())

    if code_number == 88:
        print('Hello')
    elif code_number == 86:
        print('How are you?')
    elif code_number < 88 and code_number != 86:
        print('GREAT!')
    else:
        print('Bye.')