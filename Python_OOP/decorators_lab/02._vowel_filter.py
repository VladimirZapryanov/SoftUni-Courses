import functools


def is_vowel(ch):
    return ch in "aeiouyAEIOUY"


def vowel_filter(function):
    @functools.wraps(function)
    def wrapper():
        result = function()
        return [x for x in result if is_vowel(x)]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
