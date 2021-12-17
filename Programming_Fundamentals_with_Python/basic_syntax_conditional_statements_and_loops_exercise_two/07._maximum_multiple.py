divisor = int(input())
bound = int(input())
max_number = 0

for num in range(bound + 1):
    if num % divisor == 0:
        max_number = num
print(max_number)

