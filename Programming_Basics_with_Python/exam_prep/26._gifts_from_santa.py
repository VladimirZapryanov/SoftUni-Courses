number_n = int(input())
number_m = int(input())
number_s = int(input())

for number in range(number_m, number_n - 1, -1):
    if number % 2 == 0 and number % 3 == 0:
        if number == number_s:
            break
        print(number, end=" ")
