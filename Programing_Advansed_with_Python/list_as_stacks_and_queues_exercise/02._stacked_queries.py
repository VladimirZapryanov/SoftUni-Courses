numbers_of_row = int(input())

stack = []

for _ in range(numbers_of_row):
    data = input().split()
    command = data[0]

    if command == "1":
        num = int(data[1])
        stack.append(num)
    elif command == "2":
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))

rev_stack = []
while stack:
    rev_stack.append(stack.pop())

print(", ".join([str(el) for el in rev_stack]))