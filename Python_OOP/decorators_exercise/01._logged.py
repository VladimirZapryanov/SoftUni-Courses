<<<<<<< HEAD
import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args):
        return f"you called {func.__name__}{args}" + "\n" + f"it returned {func(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
=======
import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args):
        return f"you called {func.__name__}{args}" + "\n" + f"it returned {func(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
