letters = input().lower()
searched_words = ['sand', 'water', 'fish', 'sun']
words_count = 0

for word in searched_words:
    if word in letters:
        words_count += letters.count(word)

print(words_count)