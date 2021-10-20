from collections import deque

working_bees = deque([int(el) for el in input().split()])
nectar = [int(el) for el in input().split()]
symbols = deque([el for el in input().split()])

total_honey = 0

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_bee > current_nectar:
        working_bees.appendleft(current_bee)
    elif current_bee <= current_nectar:
        symbol = symbols.popleft()
        if symbol == "+":
            total_honey += current_bee + current_nectar
        elif symbol == "-":
            total_honey += abs(current_bee - current_nectar)
        elif symbol == "*":
            total_honey += current_bee * current_nectar
        elif symbol == "/":
            if current_nectar == 0:
                total_honey += 0
            else:
                total_honey += current_bee / current_nectar


print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(bee) for bee in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(n) for n in nectar)}")