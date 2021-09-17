commands_numbers = int(input())
parking_lot = set()

for _ in range(commands_numbers):
    command, car_number = input().split(", ")

    if command == "IN":
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if parking_lot:
    [print(car) for car in parking_lot]
else:
    print("Parking Lot is Empty")
