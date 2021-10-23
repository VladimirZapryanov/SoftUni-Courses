from collections import deque

materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])

presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magics:
    current_material = materials.pop()
    current_magic = magics.popleft()
    result = current_material + current_magic
    if 100 <= result <= 199:
        presents["Gemstone"] += 1
    elif 200 <= result <= 299:
        presents["Porcelain Sculpture"] += 1
    elif 300 <= result <= 399:
        presents["Gold"] += 1
    elif 400 <= result <= 499:
        presents["Diamond Jewellery"] += 1

    elif result < 100 and result % 2 == 0:
        new_result = current_material * 2 + current_magic * 3
        if 100 <= new_result <= 199:
            presents["Gemstone"] += 1
        elif 200 <= new_result <= 299:
            presents["Porcelain Sculpture"] += 1
        elif 300 <= new_result <= 399:
            presents["Gold"] += 1
        elif 400 <= new_result <= 499:
            presents["Diamond Jewellery"] += 1

    elif result < 100 and result % 2 == 1:
        new_result = result * 2
        if 100 <= new_result <= 199:
            presents["Gemstone"] += 1
        elif 200 <= new_result <= 299:
            presents["Porcelain Sculpture"] += 1
        elif 300 <= new_result <= 399:
            presents["Gold"] += 1
        elif 400 <= new_result <= 499:
            presents["Diamond Jewellery"] += 1

    elif result > 499:
        new_result = result / 2
        if 100 <= new_result <= 199:
            presents["Gemstone"] += 1
        elif 200 <= new_result <= 299:
            presents["Porcelain Sculpture"] += 1
        elif 300 <= new_result <= 399:
            presents["Gold"] += 1
        elif 400 <= new_result <= 499:
            presents["Diamond Jewellery"] += 1

if presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0 or presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magics:
    print(f"Magic left: {', '.join(map(str, magics))}")

sorted_presents = sorted(presents)
for present in sorted_presents:
    if presents[present] > 0:
        print(f"{present}: {presents[present]}")


