<<<<<<< HEAD
import re

num = int(input())

pattern = r"^(?P<surr>\|)(?P<boss>[A-Z]{4,})(?P=surr):(?P<sep>#)(?P<title>[A-Z-a-z]+ [A-Za-z]+)(?P=sep)$"

for i in range(num):
    valid = False
    command = input()
    boss_title = re.finditer(pattern,command)
    for m in boss_title:
        print(f"{m.group('boss')}, The {m.group('title')}\n"
              f" >> Strength: {len(m.group('boss'))}\n"
              f" >> Armor: {len(m.group('title'))}")
        valid = True
    if not valid:
=======
import re

num = int(input())

pattern = r"^(?P<surr>\|)(?P<boss>[A-Z]{4,})(?P=surr):(?P<sep>#)(?P<title>[A-Z-a-z]+ [A-Za-z]+)(?P=sep)$"

for i in range(num):
    valid = False
    command = input()
    boss_title = re.finditer(pattern,command)
    for m in boss_title:
        print(f"{m.group('boss')}, The {m.group('title')}\n"
              f" >> Strength: {len(m.group('boss'))}\n"
              f" >> Armor: {len(m.group('title'))}")
        valid = True
    if not valid:
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
        print('Access denied!')