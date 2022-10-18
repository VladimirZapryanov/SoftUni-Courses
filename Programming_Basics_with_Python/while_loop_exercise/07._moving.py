width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())
command = input()

free_space = width_of_free_space * length_of_free_space * height_of_free_space

while not command == "Done":
    num_of_boxes = int(command)
    free_space -= num_of_boxes

    if free_space < 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break

    command = input()

if free_space >= 0:
    print(f'{free_space} Cubic meters left.')


