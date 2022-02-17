from itertools import permutations


def possible_permutations(numbers):
    perm = permutations(numbers)
    for i in perm:
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]