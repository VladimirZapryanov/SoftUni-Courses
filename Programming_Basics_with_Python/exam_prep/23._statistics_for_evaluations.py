numbers_of_student = int(input())

group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
total_score = 0

for student in range(numbers_of_student):
    score = float(input())
    total_score += score
    if score >= 5:
        group_1 += 1
    elif 4 <= score < 5:
        group_2 += 1
    elif 3 <= score < 4:
        group_3 += 1
    elif score < 3:
        group_4 += 1

average_score = total_score / numbers_of_student

print(f"Top students: {((group_1 / numbers_of_student) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((group_2 / numbers_of_student) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((group_3 / numbers_of_student) * 100):.2f}%")
print(f"Fail: {((group_4 / numbers_of_student) * 100):.2f}%")
print(f"Average: {average_score:.2f}")

