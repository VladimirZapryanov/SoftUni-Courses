def insertion_sort(numbers):
    for i in range(len(numbers)):
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1

    return numbers


numbers = [int(x) for x in input().split(' ')]

print(*insertion_sort(numbers), sep=' ')