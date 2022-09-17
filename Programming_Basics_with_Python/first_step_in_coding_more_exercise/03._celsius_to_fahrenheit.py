def fahrenheit_convert(c):
    return f'{c * 1.8 + 32:.2f}'


celsius = float(input())

print(fahrenheit_convert(celsius))