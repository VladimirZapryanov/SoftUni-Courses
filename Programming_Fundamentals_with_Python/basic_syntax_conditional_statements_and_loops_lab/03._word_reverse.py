#word = input()
#print(word[:: -1])

#another way!!!

word = input()
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(reversed_word)
