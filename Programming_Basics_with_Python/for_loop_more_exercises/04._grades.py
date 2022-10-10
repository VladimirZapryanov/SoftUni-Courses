students = int(input())

total_score = 0
top_students = 0
students_between_four_and_five = 0
students_between_three_and_four = 0
failed_students = 0

for s in range(1, students + 1):
    student_score = float(input())

    total_score += student_score

    if student_score >= 5:
        top_students += 1
    elif student_score >= 4:
        students_between_four_and_five += 1
    elif student_score >= 3:
        students_between_three_and_four += 1
    else:
        failed_students += 1

print(f'Top students: {top_students / students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {students_between_four_and_five / students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {students_between_three_and_four / students * 100:.2f}%')
print(f'Fail: {failed_students / students * 100:.2f}%')
print(f'Average: {total_score / students:.2f}')