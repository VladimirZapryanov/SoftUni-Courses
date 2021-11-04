import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

names = input()
valid_names = re.findall(pattern, names)

print(" ".join(valid_names))