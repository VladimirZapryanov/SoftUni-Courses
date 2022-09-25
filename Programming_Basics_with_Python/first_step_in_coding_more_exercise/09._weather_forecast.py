def weather_forecast(weather):
    if weather == 'sunny':
        return "It's warm outside!"
    else:
        return "It's cold outside!"


weather = input()

print(weather_forecast(weather))