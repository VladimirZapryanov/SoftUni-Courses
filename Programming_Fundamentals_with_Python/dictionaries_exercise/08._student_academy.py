rows = int(input())

student_dict = {}

for n in range(0, rows):
    name = input()
    grade = float(input())
    if name not in student_dict:
        student_dict[name] = []
        student_dict[name].append(grade)
    else:
        student_dict[name].append(grade)

for name in student_dict:
    avr_grade = sum(student_dict[name]) / len(student_dict[name])
    student_dict[name] = avr_grade

for name, grade in list(student_dict.items()):
    if grade < 4.50:
        del student_dict[name]

sorted_dict = {k: v for k, v in sorted(student_dict.items(), key=lambda item: -item[1])}

for name, grade in sorted_dict.items():
    print(f"{name} -> {grade:.2f}")


