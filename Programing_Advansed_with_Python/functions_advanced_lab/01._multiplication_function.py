def multiply(*args):
    result = 1
    if len(args) < 1:
        return None
    for el in args:
        result *= el
    return result


'''
some test:
print(multiply())
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
'''




