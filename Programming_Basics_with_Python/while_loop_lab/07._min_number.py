import sys
min = sys.maxsize
command = input()
while command != "Stop":
    number = int(command)
    if number < min:
        min = number
    command = input()
print(min)