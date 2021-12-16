import math

count_of_student = int(input())
count_of_lecture = int(input())
initial_bonus = float(input())

max_bonus = 0
max_lecture = 0
for student in range(count_of_student):
    attendances_of_each_student = int(input())
    total_bonus = (attendances_of_each_student * 1.00) / (count_of_lecture * 1.00) * \
                  (5 * 1.00 + initial_bonus * 1.00)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        max_lecture = attendances_of_each_student

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_lecture} lectures.")
