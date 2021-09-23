count_of_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
for number in range(count_of_numbers):
    current_number = int(input())
    if current_number % 2 == 0:
        p1 += 1
    if current_number % 3 == 0:
        p2 += 1
    if current_number % 4 == 0:
        p3 += 1
print(f"{p1 / count_of_numbers * 100:.2f}%")
print(f"{p2 / count_of_numbers * 100:.2f}%")
print(f"{p3 / count_of_numbers * 100:.2f}%")
