from collections import deque

quantity_of_the_food = int(input())
quantity_of_an_order = input().split()

order_queue = deque()
max_order = max([int(el) for el in quantity_of_an_order])

for el in quantity_of_an_order:
    order_queue.append(el)

while order_queue:
    current_order = int(order_queue.popleft())
    if quantity_of_the_food < current_order:
        order_queue.appendleft(current_order)
        break
    else:
        quantity_of_the_food -= current_order

print(max_order)
if order_queue:
    print(f"Orders left: {' '.join([str(el) for el in order_queue])}")
else:
    print("Orders complete")