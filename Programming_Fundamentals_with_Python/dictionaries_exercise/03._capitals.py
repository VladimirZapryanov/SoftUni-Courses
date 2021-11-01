country = input().split(", ")
cities = input().split(", ")

country_cities = zip(country, cities)
new_country_cities = {country: cities for country, cities in country_cities}

for country, cities in new_country_cities.items():
    print(f"{country} -> {cities}")

