target_height = int(input())

stick_height = target_height - 30
total_jumps = 0
fail = False
while stick_height <= target_height and not fail:
    fail_jumps = 0

    for jump in range(1, 4):
        total_jumps += 1
        jump_height = int(input())
        if stick_height >= jump_height:
            fail_jumps += 1
            if fail_jumps == 3:
                fail = True
                break
        else:
            stick_height += 5
            break

if fail:
    print(f"Tihomir failed at {stick_height}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {target_height}cm after {total_jumps} jumps.")



