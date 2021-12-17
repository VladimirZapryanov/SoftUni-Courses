first_string = input()
second_string = input()
last_string = first_string

for symbol in range(len(first_string)):
    left_part = second_string[:symbol + 1]
    right_part = first_string[symbol + 1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string


