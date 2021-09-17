numbers_of_students = int(input())

students = {}

for _ in range(numbers_of_students):
    student, grade_string = input().split()
    grade = float(grade_string)

    if student not in students:
        students[student] = []

    students[student].append(grade)

for el in students:
    avg_grade = sum([float(el) for el in students[el]]) / len(students[el])
    grade_str = ' '.join(str(f"{x:.2f}") for x in students[el])
    print(f"{el} -> {grade_str} (avg: {avg_grade:.2f})")
