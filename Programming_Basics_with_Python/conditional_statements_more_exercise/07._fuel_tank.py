def fill_tank(type_of_fuel, tank_fuel_litters, minimum_fuel, permitted_fuels):
    if type_of_fuel in permitted_fuels:
        if tank_fuel_litters >= minimum_fuel:
            return f'You have enough {type_of_fuel.lower()}.'
        elif tank_fuel_litters < minimum_fuel:
            return f'Fill your tank with {type_of_fuel.lower()}!'
    else:
        return 'Invalid fuel!'


type_of_fuel = input()
tank_fuel_litters = float(input())

permitted_fuels = ['Diesel', 'Gasoline', 'Gas']
minimum_fuel = 25

print(fill_tank(type_of_fuel, tank_fuel_litters, minimum_fuel, permitted_fuels))
