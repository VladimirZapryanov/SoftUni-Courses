line = input()
conditions = [x.strip() for x in line.replace("?", ":").split(":")]
idxs = [i for i, j in enumerate(conditions) if j in {"t", "f"}][::-1]

for idx in idxs:
    if conditions[idx] == "t":
        del conditions[idx + 2]
    else:
        del conditions[idx + 1]
    del conditions[idx]

print(conditions[0])

