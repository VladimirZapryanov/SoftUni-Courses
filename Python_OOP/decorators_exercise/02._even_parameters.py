<<<<<<< HEAD
import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args):
        if all([isinstance(x, int) and x % 2 == 0 for x in args]):
            return func(*args)
        else:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
=======
import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args):
        if all([isinstance(x, int) and x % 2 == 0 for x in args]):
            return func(*args)
        else:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
