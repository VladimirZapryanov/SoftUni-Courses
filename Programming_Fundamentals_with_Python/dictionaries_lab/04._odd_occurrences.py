words = input().split(" ")

words_count = {}

for word in words:
    lower_word = word.lower()
    if lower_word not in words_count:
        words_count[lower_word] = 1
    else:
        words_count[lower_word] += 1

for key, value in words_count.items():
    if value % 2 == 1:
        print(key, end=" ")
