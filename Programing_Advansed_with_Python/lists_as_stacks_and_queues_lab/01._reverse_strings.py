string = input()

ss = []
result = ""

for el in string:
    ss.append(el)

while len(ss) > 0:
    result += ss.pop()

print(result)