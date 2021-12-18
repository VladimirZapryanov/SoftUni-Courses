lines = int(input())
water_tank_capacity = 255
water_in_tank = 0

for line in range(1, lines + 1):
    liters_of_water = int(input())
    water_in_tank += liters_of_water
    if water_in_tank > water_tank_capacity:
        print("Insufficient capacity!")
        water_in_tank -= liters_of_water
print(water_in_tank)
