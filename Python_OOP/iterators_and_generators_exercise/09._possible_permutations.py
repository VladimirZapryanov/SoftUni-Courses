<<<<<<< HEAD
from itertools import permutations


def possible_permutations(numbers):
    perm = permutations(numbers)
    for i in perm:
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]
=======
from itertools import permutations


def possible_permutations(numbers):
    perm = permutations(numbers)
    for i in perm:
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
[print(n) for n in possible_permutations([1])]