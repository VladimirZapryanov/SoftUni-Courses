import functools


def cache(func):
    log = {}

    @functools.wraps(func)
    def wrapper(n):
        if n in log:
            return log[n]
        else:
            log[n] = func(n)
            return log[n]

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
