failed_limit = int(input())
last_command = ''
failed_number = 0
total_tasks = 0
total_grades = 0
has_failed = True

while failed_number < failed_limit:
    command = input()
    if command == "Enough":
        has_failed = False
        break
    grade = int(input())
    total_tasks += 1
    total_grades += grade
    last_command = command
    if grade <= 4:
        failed_number += 1


average = total_grades / total_tasks

if failed_number >= failed_limit:
    print(f"You need a break, {failed_number} poor grades.")
else:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {total_tasks}")
    print(f"Last problem: {last_command}")

