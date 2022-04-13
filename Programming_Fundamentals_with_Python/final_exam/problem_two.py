<<<<<<< HEAD
import re

pattern = r'^\|(?P<name>[A-Z]{4,})\|:#(?P<title>[a-zA-Z]+ [a-zA-Z]+)#$'
n = int(input())

for _ in range(n):
    text = input()
    matches = list(re.finditer(pattern, text))
    if len(matches) > 0:
        for match in matches:
            print(f'{match.group("name")}, The {match.group("title")}\n>> Strength: {len(match.group("name"))}\n>> Armor: {len(match.group("title"))}')
    else:
=======
import re

pattern = r'^\|(?P<name>[A-Z]{4,})\|:#(?P<title>[a-zA-Z]+ [a-zA-Z]+)#$'
n = int(input())

for _ in range(n):
    text = input()
    matches = list(re.finditer(pattern, text))
    if len(matches) > 0:
        for match in matches:
            print(f'{match.group("name")}, The {match.group("title")}\n>> Strength: {len(match.group("name"))}\n>> Armor: {len(match.group("title"))}')
    else:
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
        print('Access denied!')