import os


result = {}

for root, _, files in os.walk(os.getcwd()):
    for file in files:
        ext = file.split(".")[-1]
        if ext not in result:
            result[ext] = []
            result[ext].append(os.path.join(root, file))

print(result)