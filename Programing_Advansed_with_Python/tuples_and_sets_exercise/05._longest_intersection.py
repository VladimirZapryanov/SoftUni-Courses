numbers_of_row = int(input())

longest_set = set()

for _ in range(numbers_of_row):
    first_numbers, second_numbers = input().split("-")

    first_start, first_end = first_numbers.split(",")
    second_start, second_end = second_numbers.split(",")

    first_set = set(range(int(first_start), int(first_end) + 1))
    second_set = set(range(int(second_start), int(second_end) + 1))
    current_set = first_set.intersection(second_set)

    if len(current_set) > len(longest_set):
        longest_set = current_set


print(f"Longest intersection is [{', '.join(str(el) for el in longest_set)}] with length {len(longest_set)}")

