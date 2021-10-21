substring = input().split("|")

result = []

for x in range(len(substring) - 1, -1, -1):
    elements = substring[x].split()
    result += elements

print(" ".join(result))