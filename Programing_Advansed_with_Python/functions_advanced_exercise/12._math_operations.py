from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    result = kwargs
    while numbers:
        result["a"] += numbers.popleft()
        if numbers:
            result["s"] -= numbers.popleft()
        if numbers:
            if numbers[0] == 0:
                numbers.popleft()
            else:
                result["d"] /= numbers.popleft()
        if numbers:
            result["m"] *= numbers.popleft()

    return result


"""
some test:
print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
"""


