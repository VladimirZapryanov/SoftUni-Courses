def merge_arrays(left, right):
    sorted_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted_array.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_array.append(right[right_index])
        right_index += 1

    return sorted_array


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    middle_index = len(numbers) // 2
    left = numbers[:middle_index]
    right = numbers[middle_index:]

    return merge_arrays(merge_sort(left), merge_sort(right))


numbers = [int(x) for x in input().split()]
print(*merge_sort(numbers), sep=' ')

