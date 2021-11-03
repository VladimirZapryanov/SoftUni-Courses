string = input()

for char in range(len(string)):
    if string[char] == ":":
        new_char = string[char] + string[char + 1]
        print(new_char)

