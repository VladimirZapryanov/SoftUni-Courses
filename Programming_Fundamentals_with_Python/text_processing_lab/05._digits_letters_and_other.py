string = input()

digits = ""
letters = ""
other_char = ""


for ch in string:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        other_char += ch

print(digits)
print(letters)
print(other_char)
