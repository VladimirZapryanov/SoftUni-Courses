from math import floor


def total_working_space(w_in_metter, h_in_metter, space_for_door, space_for_department, space_for_corridor_in_centimeters, w_space_for_one, h_space_for_one):
    w_in_centimeters = (w_in_metter * 100)
    h_in_centimeters = (h_in_metter * 100) - space_for_corridor_in_centimeters
    w_free_space = floor(w_in_centimeters / w_space_for_one)
    h_free_space = floor(h_in_centimeters / h_space_for_one)
    return (w_free_space * h_free_space) - (space_for_door + space_for_department)


w_in_metter = float(input())
h_in_metter = float(input())

space_for_door = 1
space_for_department = 2
space_for_corridor_in_centimeters = 100
h_space_for_one = 70
w_space_for_one = 120

print(total_working_space(w_in_metter, h_in_metter, space_for_door, space_for_department, space_for_corridor_in_centimeters, w_space_for_one, h_space_for_one))


