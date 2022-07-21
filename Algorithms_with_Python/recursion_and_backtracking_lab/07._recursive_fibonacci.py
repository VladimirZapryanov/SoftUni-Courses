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
