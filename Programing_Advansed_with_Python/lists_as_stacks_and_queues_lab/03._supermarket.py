<<<<<<< HEAD
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
=======
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
>>>>>>> 70ad78d340a318b5f1bce2a4b82c6b4d0f40d434
