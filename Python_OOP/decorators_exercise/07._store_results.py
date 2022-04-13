<<<<<<< HEAD
class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        with open("results.txt", "a") as file:
            output = f"Function '{self.func.__name__}' was called. Result: {self.func(*args)}"
            file.write(output)
            file.write("\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
=======
class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        with open("results.txt", "a") as file:
            output = f"Function '{self.func.__name__}' was called. Result: {self.func(*args)}"
            file.write(output)
            file.write("\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
