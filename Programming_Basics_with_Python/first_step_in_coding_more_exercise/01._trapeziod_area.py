def trapeziod_area(b1, b2, h):
    return f'{(b1 + b2) * h / 2:.2f}'


b1 = float(input())
b2 = float(input())
h = float(input())

print(trapeziod_area(b1, b2, h))