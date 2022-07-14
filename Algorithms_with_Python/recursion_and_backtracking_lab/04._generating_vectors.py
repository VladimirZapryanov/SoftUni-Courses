def generating_vectors(index, vector):
    if index >= len(vector):
        print(''.join([str(x) for x in vector]))
        return
    for number in range(0, 2):
        vector[index] = number
        generating_vectors(index + 1, vector)


n = int(input())
array = [None] * n

generating_vectors(0, array)
