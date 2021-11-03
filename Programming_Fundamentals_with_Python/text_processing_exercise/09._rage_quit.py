line = input().upper()
index = 0
new_line = ""
while index < len(line):
    piece = ""
    len_num = ""
    num = 0
    while not line[index].isdigit():
        piece += line[index]
        index += 1
    while line[index].isdigit():
        len_num += line[index]
        index += 1
        if index == len(line):
            break
    num = int(len_num)
    new_line += piece * num
unique = len(''.join(set(new_line)))
print(f"Unique symbols used: {unique}")
print(new_line)