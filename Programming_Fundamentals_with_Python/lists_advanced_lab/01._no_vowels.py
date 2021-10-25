vowels = ["a", "o", "u", "e", "i"]
text = input()

print("".join([symbol for symbol in text if symbol.lower() not in vowels]))


