import functools


def is_even(number):
    if number % 2 == 0:
        return number


def even_numbers(function):

    @functools.wraps(function)
    def wrapper(numbers):
        return [n for n in numbers if is_even(n)]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))




