command = input()
numbers = [int(x) for x in input().split()]

parity = 0 if command == "Even" else 1
filtered_sum = sum(filter(lambda x: x % 2 == parity, numbers))

print(filtered_sum * len(numbers))
