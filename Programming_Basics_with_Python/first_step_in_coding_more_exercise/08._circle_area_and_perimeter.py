from math import pi


def circle_area(r):
    return f'{pi * r**2:.2f}'


def circle_perimeter(r):
    return f'{2 * (pi * r):.2f}'


r = float(input())

print(circle_area(r))
print(circle_perimeter(r))
