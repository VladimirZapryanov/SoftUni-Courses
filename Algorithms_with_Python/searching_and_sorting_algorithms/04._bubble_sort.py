def bubble_sort(numbers):
    is_sorted = False
    i = 0
    while not is_sorted:
        is_sorted = True
        for j in range(1, len(numbers) - i):
            if numbers[j - 1] > numbers[j]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
                is_sorted = False
        i += 1

    return numbers


numbers = [int(x) for x in input().split(' ')]

print(*bubble_sort(numbers), sep=' ')
