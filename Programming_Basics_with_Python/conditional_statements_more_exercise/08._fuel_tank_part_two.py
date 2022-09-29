def fill_tank(type_of_fuel, litters_fuel, has_discount_card, gasoline_price, diesel_price, gas_price, discount_gasoline, discount_gas, more_discount, biggest_discount, min_litters_for_more_discount, min_litters_for_biggest_discount):
    fuel_price = 0

    if type_of_fuel == 'Gasoline':
        if has_discount_card == 'Yes':
            gasoline_price -= discount_gasoline
            fuel_price = gasoline_price * litters_fuel
        else:
            fuel_price = gasoline_price * litters_fuel
    elif type_of_fuel == 'Diesel':
        if has_discount_card == 'Yes':
            diesel_price -= discount_diesel
            fuel_price = diesel_price * litters_fuel
        else:
            fuel_price = diesel_price * litters_fuel
    elif type_of_fuel == 'Gas':
        if has_discount_card == 'Yes':
            gas_price -= discount_gas
            fuel_price = gas_price * litters_fuel
        else:
            fuel_price = gas_price * litters_fuel

    if min_litters_for_more_discount <= litters_fuel <= min_litters_for_biggest_discount:
        fuel_price = fuel_price - (fuel_price * more_discount)
    elif litters_fuel > min_litters_for_biggest_discount:
        fuel_price = fuel_price - (fuel_price * biggest_discount)

    return f'{fuel_price:.2f} lv.'


type_of_fuel = input()
litters_fuel = float(input())
has_discount_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
discount_gasoline = 0.18
discount_diesel = 0.12
discount_gas = 0.08
min_litters_for_more_discount = 20
min_litters_for_biggest_discount = 25
more_discount = 8 / 100
biggest_discount = 10 / 100

print(fill_tank(type_of_fuel, litters_fuel, has_discount_card, gasoline_price, diesel_price, gas_price, discount_gasoline, discount_gas, more_discount, biggest_discount, min_litters_for_more_discount, min_litters_for_biggest_discount))
