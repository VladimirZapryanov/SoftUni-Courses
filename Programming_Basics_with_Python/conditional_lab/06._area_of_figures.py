from math import pi
kind_of_figures = input()
if kind_of_figures == "square":
    side_length = float(input())
    area_of_square = side_length * side_length
    print(f"{area_of_square:.3f}")
elif kind_of_figures == "rectangle":
    side_length_of_rectangle_1 = float(input())
    side_length_of_rectangle_2 = float(input())
    area_of_rectangle = side_length_of_rectangle_1 * side_length_of_rectangle_2
    print(f"{area_of_rectangle:.3f}")
elif kind_of_figures == "circle":
    radius_of_circle = float(input())
    area_of_circle = pi * (radius_of_circle * radius_of_circle)
    print(f"{area_of_circle:.3f}")
elif kind_of_figures == "triangle":
    side_length_of_triangle = float(input())
    height_length_of_triangle = float(input())
    area_of_triangle = 0.5 * (side_length_of_triangle * height_length_of_triangle)
    print(f"{area_of_triangle:.3f}")
