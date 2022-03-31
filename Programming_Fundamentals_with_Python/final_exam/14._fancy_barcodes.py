import re

pattern = r"@#+(?P<product>[A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

lines = int(input())

for el in range(lines):
    barcode = input()
    valid_barcode = list(re.finditer(pattern, barcode))
    if len(valid_barcode) > 0:
        for match in valid_barcode:
            if match.group("product").isalpha():
                print("Product group: 00")
            else:
                print(f"Product group: {''.join([el for el in match.group('product') if el.isdigit()])}")
    else:
        print("Invalid barcode")

