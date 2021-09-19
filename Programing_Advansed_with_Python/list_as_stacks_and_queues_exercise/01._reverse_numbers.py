string = input().split()

reverse_string = []

while string:
    reverse_string.append(string.pop())
print(" ".join(reverse_string))

