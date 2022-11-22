<<<<<<< HEAD
letters = input().lower()
searched_words = ['sand', 'water', 'fish', 'sun']
words_count = 0

for word in searched_words:
    if word in letters:
        words_count += letters.count(word)

=======
letters = input().lower()
searched_words = ['sand', 'water', 'fish', 'sun']
words_count = 0

for word in searched_words:
    if word in letters:
        words_count += letters.count(word)

>>>>>>> d08d4ea4512bfeb4b972933d878a4e98a8505fbe
print(words_count)