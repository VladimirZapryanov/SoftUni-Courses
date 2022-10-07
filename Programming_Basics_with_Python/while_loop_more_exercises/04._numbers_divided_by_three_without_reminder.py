def divided_by_three(start_number, end_number, divided_by):
    all_numbers = []
    for num in range(start_number, end_number + 1):
        if num % divided_by == 0:
            all_numbers.append(num)
    return '\n'.join(str(x) for x in all_numbers)


start_number = 1
end_number = 100
divided_by = 3

print(divided_by_three(start_number, end_number, divided_by))