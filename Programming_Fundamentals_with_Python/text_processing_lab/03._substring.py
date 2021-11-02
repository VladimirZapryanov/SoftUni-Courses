word_one = input()
word_two = input()


while word_one in word_two:
   word_two = word_two.replace(word_one, "")

print(word_two)
