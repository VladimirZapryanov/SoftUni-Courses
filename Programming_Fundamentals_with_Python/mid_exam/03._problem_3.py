price_rating = [int(el) for el in input().split(", ")]
entry_point = int(input())
command = input()

left_side = price_rating[:entry_point]
right_side = price_rating[entry_point + 1:]

if command == "cheap":
    price_left = [el for el in left_side if el < entry_point]
    price_right = [el for el in right_side if el < entry_point]

    sum_left_side = sum(price_left)
    sum_right_side = sum(price_right)

    if sum_left_side > sum_right_side:
        position = "Left"
        print(f"{position} - {sum_left_side}")

    elif sum_right_side > sum_left_side:
        position = "Right"
        print(f"{position} - {sum_right_side}")

    else:
        position = "Left"
        print(f"{position} - {sum_left_side}")

elif command == "expensive":
    price_left = [el for el in left_side if el >= entry_point]
    price_right = [el for el in right_side if el >= entry_point]

    sum_left_side = sum(price_left)
    sum_right_side = sum(price_right)

    if sum_left_side > sum_right_side:
        position = "Left"
        print(f"{position} - {sum_left_side}")

    elif sum_right_side > sum_left_side:
        position = "Right"
        print(f"{position} - {sum_right_side}")

    else:
        position = "Left"
        print(f"{position} - {sum_left_side}")


