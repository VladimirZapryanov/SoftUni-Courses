word_one, word_two = input().split()

total_sum = 0

min_word = min(len(word_one), len(word_two))
max_word = max(len(word_one), len(word_two))

for el in range(min_word):
    num_one = ord(word_one[el])
    num_two = ord(word_two[el])
    total_sum += num_one * num_two

for el in range(min_word, max_word):
    if len(word_one) > len(word_two):
        total_sum += ord(word_one[el])
    else:
        total_sum += ord(word_two[el])

print(total_sum)
