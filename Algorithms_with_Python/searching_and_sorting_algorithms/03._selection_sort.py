def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


numbers = [int(x) for x in input().split(' ')]

print(*selection_sort(numbers), sep=' ')
