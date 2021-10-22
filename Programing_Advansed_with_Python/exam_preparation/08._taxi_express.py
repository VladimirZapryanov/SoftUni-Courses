from collections import deque

customers = deque(int(x) for x in input().split(", "))
taxis = deque(int(x) for x in input().split(", "))

total_time = 0

while customers and taxis:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()
    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")

