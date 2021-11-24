version = input().split(".")

new_version_2 = []

version_1 = "".join(version)
version_2 = int(version_1) + 1
new_version_1 = str(version_2)

for el in new_version_1:
    new_version_2.append(el)

new_version_3 = ".".join(new_version_2)

print(new_version_3)
