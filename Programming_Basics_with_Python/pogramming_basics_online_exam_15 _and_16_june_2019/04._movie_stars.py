budget = float(input())
command = input()

while command != "ACTION":
    actor_name = command
    salary = 0

    if len(actor_name) > 15:
        salary = 0.2 * budget
    else:
        salary = float(input())
    budget -= salary

    if budget <= 0:
        break
    command = input()

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")