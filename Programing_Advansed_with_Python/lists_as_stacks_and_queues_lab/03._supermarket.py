from collections import deque

command = input()

qq = deque()

while not command == "End":
    if command == "Paid":
        for el in range(len(qq)):
            print(qq.popleft())
        qq = deque()
    else:
        qq.append(command)
    command = input()

print(f"{len(qq)} people remaining.")
