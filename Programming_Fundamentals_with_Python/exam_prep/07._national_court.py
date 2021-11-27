first_employees = int(input())
second_employees = int(input())
third_employees = int(input())
people_count = int(input())

all_employees = first_employees + second_employees + third_employees
hours = 0

while people_count > 0:
    hours += 1
    people_count -= all_employees
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")