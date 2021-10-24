n = int(input())
given_word = input()

total_word = []
special_word = []

for _ in range(n):
    word = input()
    total_word.append(word)
    if given_word in word:
        special_word.append(word)

print(total_word)
print(special_word)