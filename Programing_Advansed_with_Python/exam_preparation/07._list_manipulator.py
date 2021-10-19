from collections import deque


def list_manipulator(list_of_numbers, command, part, *args):
    new_list_of_numbers = deque(list_of_numbers)
    command = command
    part = part
    if command == "remove" and part == "end" and len(args) == 0:
        new_list_of_numbers.pop()
    elif command == "remove" and part == "beginning" and len(args) == 0:
        new_list_of_numbers.popleft()
    elif command == "remove" and part == "end" and len(args) >= 0:
        if isinstance(args[0], int):
            count = int(args[0])
            for el in range(count):
                new_list_of_numbers.pop()
    elif command == "remove" and part == "beginning" and len(args) >= 0:
        if isinstance(args[0], int):
            count = int(args[0])
            for el in range(count):
                new_list_of_numbers.popleft()

    elif command == "add" and part == "beginning":
        assert len(args) > 0
        for el in range(len(args)):
            new_el = args[-1 - el]
            new_list_of_numbers.appendleft(new_el)
    elif command == "add" and part == "end":
        assert len(args) > 0
        for el in args:
            new_list_of_numbers.append(el)

    return list(new_list_of_numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
