numbers_of_cars = int(input())

cars = {}
max_fuel_capacity = 75
for car in range(numbers_of_cars):
    car_info = input().split("|")
    cars[car_info[0]] = {"mileage": int(car_info[1]), "fuel": int(car_info[2])}

commands = input()

while not commands == "Stop":
    data = commands.split(" : ")
    command = data[0]
    car = data[1]

    if command == "Drive":
        if cars[car]["fuel"] < int(data[3]):
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += int(data[2])
            cars[car]["fuel"] -= int(data[3])
            print(f"{car} driven for {int(data[2])} kilometers. {int(data[3])} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100_000:
                del cars[car]
                print(f"Time to sell the {car}!")

    elif command == "Refuel":
        cars[car]["fuel"] += int(data[2])
        if cars[car]["fuel"] > max_fuel_capacity:
            refuel = int(data[2]) - (cars[car]["fuel"] - max_fuel_capacity)
            cars[car]["fuel"] = 75
            print(f"{car} refueled with {refuel} liters")
        else:
            print(f"{car} refueled with {int(data[2])} liters")

    elif command == "Revert":
        cars[car]["mileage"] -= int(data[2])
        if cars[car]["mileage"] < 10_000:
            cars[car]["mileage"] = 10_000
        else:
            print(f"{car} mileage decreased by {int(data[2])} kilometers")

    commands = input()

sorted_cars = dict(sorted(cars.items(), key=lambda kvp: (-kvp[1]["mileage"], kvp[0])))

for cars in sorted_cars:
    print(f"{cars} -> Mileage: {sorted_cars[cars]['mileage']} kms, Fuel in the tank: {sorted_cars[cars]['fuel']} lt.")