command = input()
courses = {}

while not command == "end":
    course_name, student_name = command.split(' : ')
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    command = input()

sorted_courses = sorted(courses.items(), key=lambda kvp: -len(kvp[1]))

for course, num_of_students in sorted_courses:
    print(f"{course}: {len(num_of_students)}")
    result = sorted(num_of_students)
    for item in result:
        print(f"-- {item}")