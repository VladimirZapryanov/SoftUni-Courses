def letter_combinator(start_letter, end_letter, forbidden_letter):
    start_number = ord(start_letter)
    end_number = ord(end_letter)
    forbidden_number = ord(forbidden_letter)
    counter = 0
    all_combinations = []

    for n1 in range(start_number, end_number + 1):
        for n2 in range(start_number, end_number + 1):
            for n3 in range(start_number, end_number + 1):
                if not n1 == forbidden_number and not n2 == forbidden_number and not n3 == forbidden_number:
                    counter += 1
                    all_combinations.append(f'{chr(n1)}{chr(n2)}{chr(n3)}')

    return f"{' '.join(all_combinations)} {counter}"


start_letter = input()
end_letter = input()
forbidden_letter = input()

print(letter_combinator(start_letter, end_letter, forbidden_letter))