import re

text = input()
searched_word = input()
pattern = rf"\b{searched_word}\b"

valid_word = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(valid_word))