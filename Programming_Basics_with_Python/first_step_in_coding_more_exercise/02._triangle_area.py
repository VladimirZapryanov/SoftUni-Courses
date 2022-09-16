def triangle_area(a, h):
    return f'{a * h / 2:.2f}'


a = float(input())
h = float(input())

print(triangle_area(a, h))