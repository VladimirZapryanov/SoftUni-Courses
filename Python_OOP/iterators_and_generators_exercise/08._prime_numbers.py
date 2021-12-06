from math import sqrt, floor


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True

    boundary = floor(sqrt(number))
    for i in range(2, boundary + 1):
        if number % i == 0:
            return False

    return True


def get_primes(numbers):
    for number in numbers:
        if is_prime(number):
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))