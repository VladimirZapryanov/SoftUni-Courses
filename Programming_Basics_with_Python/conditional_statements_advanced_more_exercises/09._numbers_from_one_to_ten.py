def numbers(num_one, last_num):
    nums = []
    for num in range(num_one, last_num + 1):
        nums.append(num)

    return [str(x) for x in nums]


print('\n'.join(numbers(1, 10)))
