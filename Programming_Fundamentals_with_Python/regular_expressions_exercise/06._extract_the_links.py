import re

pattern = r"(?P<domain>www.[A-Za-z0-9\-]+\.[A-Za-z]+[A-Za-z\.]*)"


text = input()
valid_domains = []

while text:
    valid_domain = re.finditer(pattern, text)
    for el in valid_domain:
        valid_domains.append(el["domain"])
    text = input()

for el in valid_domains:
    print(el)

