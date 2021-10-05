interval_start = int(input())
interval_end = int(input())
megical_number = int(input())
combination_counter = 0
flag = False
for x in range(interval_start, interval_end + 1):
    for y in range(interval_start, interval_end + 1):
        combination = x + y
        combination_counter += 1
        if combination == megical_number:
            print(f"Combination N:{combination_counter} ({x} + {y} = {megical_number})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{combination_counter} combinations - neither equals {megical_number}")

