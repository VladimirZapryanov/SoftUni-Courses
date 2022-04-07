import re

pattern = r"(?P<separator>@|#)(?P<word>[A-Za-z]{3,})(?P=separator)(?P=separator)(?P<reverse_word>[A-Za-z]{3,})(?P=separator)"

text = input()

valid_combination = re.finditer(pattern, text)
valid_pairs_count = 0
mirror_word = []

for match in valid_combination:
    valid_pairs_count += 1
    current_match = match.groupdict()
    word = current_match["word"]
    reversed_word = current_match["reverse_word"]
    reversed_word = reversed_word[::-1]
    if word == reversed_word:
        mirror_word.append(f"{current_match['word']} <=> {current_match['reverse_word']}")

if valid_pairs_count == 0:
    print("No word pairs found!")
else:
    print(f"{valid_pairs_count} word pairs found!")
if len(mirror_word) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_word))
