import re

pattern = r"\+359(?P<separator>[-\s])2(?P=separator)\d{3}(?P=separator)\d{4}\b"
phone_numbers = input()
valid_phone_numbers = re.finditer(pattern, phone_numbers)
print(", ".join([number.group() for number in valid_phone_numbers]))
