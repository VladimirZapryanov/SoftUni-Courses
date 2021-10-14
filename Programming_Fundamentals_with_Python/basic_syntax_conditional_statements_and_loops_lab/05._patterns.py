number = int(input())
number_of_star = 0
for star in range(1, number + 1):
    number_of_star += 1
    print("*" * number_of_star)
for star in range(number + 1, 0, - 1):
    number_of_star -= 1
    print("*" * number_of_star)
