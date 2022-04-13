<<<<<<< HEAD
employee_one = int(input())
employee_two = int(input())
employee_tree = int(input())
students = int(input())

hours = 0
student_per_hour = employee_one + employee_two + employee_tree

while students > 0:
    hours += 1
    students -= student_per_hour
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")

=======
employee_one = int(input())
employee_two = int(input())
employee_tree = int(input())
students = int(input())

hours = 0
student_per_hour = employee_one + employee_two + employee_tree

while students > 0:
    hours += 1
    students -= student_per_hour
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
