numbers = [int(num) for num in input().split(", ")]

group = 10
list_of_numbers = []

while len(numbers) > 0:
    list_of_numbers = [num for num in numbers if num <= group]
    print(f"Group of {group}'s: {list_of_numbers}")
    numbers = [num for num in numbers if num > group]
    group += 10
    list_of_numbers.clear()
