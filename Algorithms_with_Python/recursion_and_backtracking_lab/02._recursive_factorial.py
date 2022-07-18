def recursive_factorial(current_element):
    if current_element == 0:
        return 1
    return current_element * recursive_factorial(current_element - 1)


num = int(input())

print(recursive_factorial(num))
