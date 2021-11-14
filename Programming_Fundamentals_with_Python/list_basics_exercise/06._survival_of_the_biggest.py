numbers_str = input().split()
n = int(input())

for i in range(len(numbers_str)):
    numbers_str[i] = int(numbers_str[i])

for i in range(n):
    min_element = min(numbers_str)
    numbers_str.remove(min_element)

for i in range(len(numbers_str)):
    numbers_str[i] = str(numbers_str[i])

print(", ".join(numbers_str))



