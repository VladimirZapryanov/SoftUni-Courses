def sum_numbers(n1, n2):
    return n1 + n2


def subtract(sum_numbers, n3):
    return sum_numbers - n3


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(subtract(sum_numbers(number_1, number_2), number_3))
