numbers_of_rooms = int(input())

num_of_room = 0
free_chairs = 0
needed_chairs_in_room = False

for room in range(numbers_of_rooms):
    num_of_room += 1
    chairs, visitor = input().split()

    if len(chairs) < int(visitor):
        print(f"{int(visitor) - len(chairs)} more chairs needed in room {num_of_room}")
        needed_chairs_in_room = True
    else:
        free_chairs += len(chairs) - int(visitor)

if not needed_chairs_in_room:
    print(f"Game On, {free_chairs} free chairs left")
