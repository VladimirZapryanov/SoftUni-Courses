total_sum = 0
command = input()
while command != "NoMoreMoney":
    sum = float(command)
    if sum < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {sum:.2f}")
        total_sum += sum
    command = input()
print(f"Total: {total_sum:.2f}")