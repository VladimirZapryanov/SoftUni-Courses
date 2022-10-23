command = input()

the_most_powerful_word = ''
strength_of_word = 0
vowel_list = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

while not command == 'End of words':
    current_word = command
    word_length = len(current_word)
    strength_of_current_word = 0

    for w in range(word_length):
        strength_of_current_word += ord(current_word[w])

    if current_word[0] in vowel_list:
        strength_of_current_word *= word_length
    else:
        strength_of_current_word = round(strength_of_current_word / word_length)

    if strength_of_current_word > strength_of_word:
        strength_of_word = strength_of_current_word
        the_most_powerful_word = current_word

    command = input()

print(f'The most powerful word is {the_most_powerful_word} - {strength_of_word}')