def fibonacci():
    number_one = 0
    number_two = 1

    yield number_one
    yield number_two

    while True:
        number_one, number_two = number_two, number_one + number_two

        yield number_two


generator = fibonacci()
for i in range(5):
     print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
