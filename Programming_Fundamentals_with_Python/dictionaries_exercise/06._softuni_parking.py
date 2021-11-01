n_of_command = int(input())

cars = {}

for n in range(0, n_of_command):
    data = input().split(" ")
    command = data[0]

    if command == "register":
        name = data[1]
        number = data[2]
        if name not in cars:
            cars[name] = number
            print(f"{name} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")

    elif command == "unregister":
        name = data[1]
        if name not in cars:
            print(f"ERROR: user {name} not found")
        else:
            del cars[name]
            print(f"{name} unregistered successfully")

for name, number in cars.items():
    print(f"{name} => {number}")




