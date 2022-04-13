<<<<<<< HEAD
import functools


def tags(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))

=======
import functools


def tags(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
