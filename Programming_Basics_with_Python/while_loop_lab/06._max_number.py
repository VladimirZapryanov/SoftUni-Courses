import sys
max = - sys.maxsize
command = input()
while command != "Stop":
    number = int(command)
    if number > max:
        max = number
    command = input()
print(max)