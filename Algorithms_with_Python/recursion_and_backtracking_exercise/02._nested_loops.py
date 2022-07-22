def nested_loops(index, array, number):
    if index >= len(array):
        print(*array, sep=' ')
        return

    for n in range(1, number + 1):
        array[index] = n
        nested_loops(index + 1, array, number)


number = int(input())
array = [None] * number
nested_loops(0, array, number)