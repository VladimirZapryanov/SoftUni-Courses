def permute(index, values):
    if index == len(values):
        print(''.join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permute(index + 1, values)
        values[i], values[index] = values[index], values[i]


values = input()
permute(0, list(values))


