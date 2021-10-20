from collections import deque

materials = deque([int(el) for el in input().split() if not int(el) == 0])
magic = deque([int(el) for el in input().split() if not int(el) == 0])

presents = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    result = current_material * current_magic

    if result == 400:
        presents["Bicycle"] += 1
    elif result == 300:
        presents["Teddy bear"] += 1
    elif result == 250:
        presents["Wooden train"] += 1
    elif result == 150:
        presents["Doll"] += 1
    elif result > 0:
        current_material += 15
        if not current_material == 0:
            materials.append(current_material)

    if result < 0:
        sum_of_values = current_material + current_magic
        if not sum_of_values == 0:
            materials.append(sum_of_values)

if presents["Teddy bear"] > 0 and presents["Bicycle"] > 0 and presents["Teddy bear"] + presents["Bicycle"] > 1 \
        or presents["Doll"] > 1 and presents["Wooden train"] > 1 and presents["Doll"] + presents["Wooden train"] > 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials.reverse()
    print(f"Materials left: {', '.join(str(el) for el in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(el) for el in magic)}")

for k, v in sorted(presents.items()):
    if presents[k] > 0:
        print(f"{k}: {v}")




