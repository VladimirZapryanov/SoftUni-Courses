numbers_of_names = int(input())

unique_names = set()

for _ in range(numbers_of_names):
    usernames = input()
    unique_names.add(usernames)

[print(n) for n in unique_names]