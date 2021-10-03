width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
count_boxes = width_free_space * length_free_space * height_free_space
house_is_over = False
command = input()

while command != "Done":
    current_boxes = int(command)
    count_boxes -= current_boxes
    if count_boxes < 0:
        house_is_over = True
        break
    command = input()
if house_is_over:
    print (f"No more free space! You need {abs(count_boxes)} Cubic meters more.")
else:
    print (f"{abs(count_boxes)} Cubic meters left.”)