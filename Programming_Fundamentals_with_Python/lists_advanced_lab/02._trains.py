train = [0] * int(input())
command = input()

while not command == "End":
    data = command.split()
    if data[0] == "add":
        train[-1] += int(data[-1])
    elif data[0] == "insert":
        train[int(data[1])] += int(data[-1])
    elif data[0] == "leave":
        train[int(data[1])] -= int(data[-1])
    command = input()

print(train)