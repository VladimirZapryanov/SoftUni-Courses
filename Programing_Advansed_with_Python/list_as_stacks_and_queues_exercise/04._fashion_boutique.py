box_with_clothes = [int(el) for el in input().split()]
capacity_of_rack = int(input())

count_of_rack = 1
current_capacity_of_rack = capacity_of_rack

while box_with_clothes:
    if current_capacity_of_rack < box_with_clothes[-1]:
        count_of_rack += 1
        current_capacity_of_rack = capacity_of_rack
    else:
        current_capacity_of_rack -= box_with_clothes.pop()

print(count_of_rack)
