happiness = [int(el) for el in input().split()]
factor = int(input())

increased_happiness = [num * factor for num in happiness]
average_happiness = sum(increased_happiness) / len(increased_happiness)

happy_employees = [people for people in increased_happiness if people >= average_happiness]
sad_employees = [people for people in increased_happiness if people < average_happiness]

if len(happy_employees) >= len(sad_employees):
    print(f"Score: {len(happy_employees)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(happiness)}. Employees are not happy!")