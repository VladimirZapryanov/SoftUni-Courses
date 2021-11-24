part_words = input().split(", ")
words = input().split(", ")

new_list = []

for el in part_words:
    for elm in words:
        if el in elm:
            if el in new_list:
                continue
            new_list.append(el)

print(new_list)