text = input()
encrypted_text = ""

for ch in text:
    new_ch = chr(ord(ch) + 3)
    encrypted_text += new_ch

print(encrypted_text)