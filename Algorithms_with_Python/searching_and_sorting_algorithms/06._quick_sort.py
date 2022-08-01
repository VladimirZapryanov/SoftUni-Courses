def quick_sort(start, end, numbers):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if numbers[left] > numbers[pivot] > numbers[right]:
            numbers[left], numbers[right] = numbers[right], numbers[left]
        if numbers[left] <= numbers[pivot]:
            left += 1
        if numbers[right] >= numbers[pivot]:
            right -= 1

    numbers[pivot], numbers[right] = numbers[right], numbers[pivot]
    quick_sort(start, right - 1, numbers)
    quick_sort(left, end, numbers)

    return numbers


numbers = [int(x) for x in input().split()]

print(*quick_sort(0, len(numbers) - 1, numbers), sep=' ')


