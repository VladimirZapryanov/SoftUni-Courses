def needed_paint(x, y, h, door_width, door_height, window_side, green_paint, red_paint):
    door_size = door_width * door_height
    windows_size = window_side**2 * 2
    front_and_back_side = x**2 * 2 - door_size
    left_and_right_side = (x * y) * 2 - windows_size
    needed_green_paint = (front_and_back_side + left_and_right_side) / green_paint

    left_and_right_side_roof = (x * y) * 2
    front_and_back_side_roof = (x * h / 2) * 2
    needed_red_paint = (left_and_right_side_roof + front_and_back_side_roof) / red_paint

    return f'{needed_green_paint:.2f}\n{needed_red_paint:.2f}'


x = float(input())
y = float(input())
h = float(input())

door_width = 1.2
door_height = 2
window_side = 1.5
green_paint = 3.4
red_paint = 4.3

print(needed_paint(x, y, h, door_width, door_height, window_side, green_paint, red_paint))
