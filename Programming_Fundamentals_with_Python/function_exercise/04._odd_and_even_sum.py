def odd_and_even_sum(number):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0

    for symbol in number:
        digit = int(symbol)
        if digit % 2 == 0:
            sum_of_even_digits += digit
        else:
            sum_of_odd_digits += digit
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


single_number = input()
print(odd_and_even_sum(single_number))

