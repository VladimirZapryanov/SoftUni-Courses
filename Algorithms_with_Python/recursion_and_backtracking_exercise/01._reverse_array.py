def reverse_array(index, array):
    if index == len(array) // 2:
        return

    swap_index = len(array) - 1 - index
    array[index], array[swap_index] = array[swap_index], array[index]
    reverse_array(index + 1, array)


array = input().split(' ')

reverse_array(0, array)
print(' '.join(array))


