from collections import deque

kids_name = input().split()
kids_name_queue = deque()
for k in kids_name:
    kids_name_queue.appendleft(k)

step = int(input())

while kids_name_queue:
    for _ in range(step - 1):
        kids_name_queue.appendleft(kids_name_queue.pop())
    kid_to_remove = kids_name_queue.pop()

    if kids_name_queue:
        print(f"Removed {kid_to_remove}")
    else:
        print(f"Last is {kid_to_remove}")

