class Calculator:

    @staticmethod
    def add(*args):
        all_args = args
        result = sum(all_args)

        return result

    @staticmethod
    def multiply(*args):
        all_args = args
        result = all_args[0]

        if args:
            for arg in all_args[1:]:
                result *= arg

        return result

    @staticmethod
    def divide(*args):
        all_args = args
        result = all_args[0]

        if args:
            for arg in all_args[1:]:
                result /= arg

        return result

    @staticmethod
    def subtract(*args):
        all_args = args
        result = all_args[0]

        if args:
            for arg in all_args[1:]:
                result -= arg

        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
