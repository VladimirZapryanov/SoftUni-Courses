sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
command = input()
while command != "stop":
    is_Prime = True
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        command = int(input())
        continue
    for number in range(2, current_number):
        if current_number % number == 0:
            is_Prime = False
            break
    if is_Prime:
        sum_of_prime_numbers += current_number
    else:
        sum_of_prime_numbers += current_number
    command = input()
print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")