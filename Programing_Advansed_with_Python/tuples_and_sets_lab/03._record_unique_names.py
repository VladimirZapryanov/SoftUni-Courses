numbers_of_names = int(input())

unique_names = set()

for _ in range(numbers_of_names):
    name = input()
    unique_names.add(name)

#print('\n'.join(unique_names))

[print(name) for name in unique_names]