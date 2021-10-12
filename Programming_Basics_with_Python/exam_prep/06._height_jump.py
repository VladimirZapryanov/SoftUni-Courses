target_height = int(input())
stick_height = target_height - 30
count_all_jumps = 0
while stick_height <= target_height:
    count_fail_jumps = 0
    for jump in range(1, 4):
        count_all_jumps += 1
        jump_height = int(input())
        if jump_height > stick_height:
            stick_height += 5
            break
        else:
            count_fail_jumps += 1
    if count_fail_jumps == 3:
        print(f"Tihomir failed at {stick_height}cm after {count_all_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {target_height}cm after {count_all_jumps} jumps.")

