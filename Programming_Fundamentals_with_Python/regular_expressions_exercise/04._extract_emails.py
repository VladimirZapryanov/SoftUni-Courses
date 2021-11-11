import re

pattern = r'\s(?P<email>(?P<user>[A-Za-z0-9]+[A-Za-z0-9\.\-\_]*)\@(?P<host>[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z]+[A-Za-z\-]*)+))'

text = input()
valid_email = re.finditer(pattern, text)
for email in valid_email:
    print(email.group("email"))
