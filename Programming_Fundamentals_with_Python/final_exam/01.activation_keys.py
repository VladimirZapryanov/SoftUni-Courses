raw_activation_key = input()

operation = input()

while not operation == "Generate":
    operation = operation.split(">>>")
    if operation[0] == "Contains":
        if operation[1] in raw_activation_key:
            print(f"{raw_activation_key} contains {operation[1]}")
        else:
            print("Substring not found!")
    elif operation[0] == "Flip":
        left_part = raw_activation_key[:int(operation[2])]
        middle_part = raw_activation_key[int(operation[2]):int(operation[3])]
        right_part = raw_activation_key[int(operation[3]):]
        if operation[1] == "Upper":
            middle_part = str(middle_part).upper()
            raw_activation_key = left_part + middle_part + right_part
        elif operation[1 == "Lower"]:
            middle_part = str(middle_part).lower()
            raw_activation_key = left_part + middle_part + right_part
        print(raw_activation_key)
    elif operation[0] == "Slice":
        left_part = raw_activation_key[:int(operation[1])]
        right_part = raw_activation_key[int(operation[2]):]
        raw_activation_key = left_part + right_part
        print(raw_activation_key)
    operation = input()

print(f"Your activation key is: {raw_activation_key}")