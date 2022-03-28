def read_next(*args):
    for iterable in args:
        for ch in iterable:
            yield ch


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')



