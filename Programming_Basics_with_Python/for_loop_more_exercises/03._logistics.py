numbers_of_cargo = int(input())

bus_price_per_ton = 200
truck_price_per_ton = 175
train_price_per_ton = 120

total_cost = 0
total_cargo = 0
bus_cargo = 0
truck_cargo = 0
train_cargo = 0

for c in range(1, numbers_of_cargo + 1):
    cargo = int(input())

    if cargo <= 3:
        total_cost += cargo * bus_price_per_ton
        total_cargo += cargo
        bus_cargo += cargo
    elif cargo <= 11:
        total_cost += cargo * truck_price_per_ton
        total_cargo += cargo
        truck_cargo += cargo
    else:
        total_cost += cargo * train_price_per_ton
        total_cargo += cargo
        train_cargo += cargo

average_cost = total_cost / total_cargo
bus_percentage = bus_cargo / total_cargo * 100
truck_percentage = truck_cargo / total_cargo * 100
train_percentage = train_cargo / total_cargo * 100

print(f'{average_cost:.2f}')
print(f'{bus_percentage:.2f}%')
print(f'{truck_percentage:.2f}%')
print(f'{train_percentage:.2f}%')