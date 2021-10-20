from collections import deque
from math import floor

string = input().split()
current_numbers = deque()
sign = ["-", "+", "/", "*"]

for el in string:
    if el not in sign:
        current_numbers.append(int(el))
    elif el == "+":
        sum_of_numbers = sum(current_numbers)
        current_numbers.clear()
        current_numbers.append(sum_of_numbers)
    elif el == "-":
        for i in range(len(current_numbers) - 1):
            subtraction_numbers = current_numbers.popleft() - current_numbers.popleft()
            current_numbers.appendleft(subtraction_numbers)
    elif el == "*":
        for i in range(len(current_numbers) - 1):
            multiplication_numbers = current_numbers.popleft() * current_numbers.popleft()
            current_numbers.appendleft(multiplication_numbers)
    elif el == "/":
        for i in range(len(current_numbers) - 1):
            division_numbers = floor(current_numbers.popleft() / current_numbers.popleft())
            current_numbers.appendleft(division_numbers)

current_numbers = list(current_numbers)
print("".join(str(el) for el in current_numbers))
