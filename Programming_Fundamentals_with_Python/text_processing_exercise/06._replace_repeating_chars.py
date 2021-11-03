text = input()
new_text = ""

for el in text:
    if el not in new_text:
        new_text += el
    elif el not in new_text[-1]:
        new_text += el

print(new_text)
