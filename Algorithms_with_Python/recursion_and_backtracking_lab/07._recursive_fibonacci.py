<<<<<<< HEAD
def fibonacci(number):
    first_number = 1
    second_number = 1

    result = 0
    for _ in range(number - 1):
        result = first_number + second_number
        first_number, second_number = second_number, result

    return result


number = int(input())
print(fibonacci(number))
=======
def fibonacci(number):
    first_number = 1
    second_number = 1

    result = 0
    for _ in range(number - 1):
        result = first_number + second_number
        first_number, second_number = second_number, result

    return result


number = int(input())
print(fibonacci(number))
>>>>>>> d3c4cae3bda419f81a33f7ff9feecc4e08780098
