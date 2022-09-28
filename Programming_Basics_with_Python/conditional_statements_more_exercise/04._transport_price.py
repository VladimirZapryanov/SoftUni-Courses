def transport_price(kilometers, time, taxi_first_fee, taxi_day_fee_per_km, taxi_night_fee_per_km, bus_minimum_km, train_minimum_km, bus_fee_per_km, train_fee_per_km):
    money = 0

    if kilometers >= train_minimum_km:
        money += kilometers * train_fee_per_km
    elif kilometers >= bus_minimum_km:
        money += kilometers * bus_fee_per_km
    else:
        money += taxi_first_fee
        if time == 'day':
            money += kilometers * taxi_day_fee_per_km
        elif time == 'night':
            money += kilometers * taxi_night_fee_per_km

    return f'{money:.2f}'


kilometers = int(input())
time = input()

taxi_first_fee = 0.70
taxi_day_fee_per_km = 0.79
taxi_night_fee_per_km = 0.90

bus_minimum_km = 20
bus_fee_per_km = 0.09

train_minimum_km = 100
train_fee_per_km = 0.06

print(transport_price(kilometers, time, taxi_first_fee, taxi_day_fee_per_km, taxi_night_fee_per_km, bus_minimum_km, train_minimum_km, bus_fee_per_km, train_fee_per_km))
