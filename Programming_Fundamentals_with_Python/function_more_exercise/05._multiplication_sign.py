def multiplication_sign(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0 and n1 != 0 and n2 != 0 and n3 != 0:
        return "negative"
    elif n1 == 0 or n2 == 0 or n3 == 0:
        return "zero"
    elif n1 > 0 and n2 > 0 and n3 > 0:
        return "positive"


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(multiplication_sign(number_1, number_2, number_3))
