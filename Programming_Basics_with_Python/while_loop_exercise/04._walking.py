target_steps = 10000
total_steps = 0
going_home = False
while total_steps < target_steps:
    command = input()
    if command == "Going home":
        going_home = True
        break
    current_steps = int(command)
    total_steps += current_steps
if going_home:
    last_steps = int(input())
    total_steps += last_steps
difference = abs(total_steps - target_steps)
if total_steps >= target_steps:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")