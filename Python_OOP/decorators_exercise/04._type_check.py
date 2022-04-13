<<<<<<< HEAD
import functools


def type_check(types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if isinstance(*args, types):
                return func(*args)
            else:
                return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
=======
import functools


def type_check(types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if isinstance(*args, types):
                return func(*args)
            else:
                return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
