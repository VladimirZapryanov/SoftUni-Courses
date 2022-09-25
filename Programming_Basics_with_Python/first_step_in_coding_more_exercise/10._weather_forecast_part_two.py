def weather_forecast(temperature):
    if 5 <= temperature < 12:
        return 'Cold'
    elif 12 <= temperature < 15:
        return 'Cool'
    elif 15 <= temperature < 20.1:
        return 'Mild'
    elif 20.1 <= temperature < 26:
        return 'Warm'
    elif 26 <= temperature < 35:
        return 'Hot'
    else:
        return 'unknown'


temperature = float(input())

print(weather_forecast(temperature))