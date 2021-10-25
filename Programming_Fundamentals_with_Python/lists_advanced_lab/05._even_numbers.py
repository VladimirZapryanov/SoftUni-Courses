numbers = [int(el) for el in input().split(", ")]

print([index for index in range(len(numbers)) if numbers[index] % 2 == 0])
