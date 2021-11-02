data = input().split()

new_data = ""

for word in data:
    new_word = word * len(word)
    new_data += new_word

print(new_data)
