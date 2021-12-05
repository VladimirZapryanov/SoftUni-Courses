def squares(n):
    for x in range(1, n + 1):
        yield x ** 2


print(list(squares(5)))
