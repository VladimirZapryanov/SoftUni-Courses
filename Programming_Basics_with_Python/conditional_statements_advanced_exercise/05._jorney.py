budget = float(input())
season = input()
destination = ""
accomodation = ""
accomodation_price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accomodation = "Camp"
        accomodation_price = 0.3 * budget
    elif season == "winter":
        accomodation = "Hotel"
        accomodation_price = 0.7 * budget
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accomodation = "Camp"
        accomodation_price = 0.4 * budget
    elif season == "winter":
        accomodation = "Hotel"
        accomodation_price = 0.8 * budget
else:
    destination = "Europe"
    accomodation = "Hotel"
    accomodation_price = 0.9 * budget

print(f"Somewhere in {destination}")
print(f"{accomodation} - {accomodation_price:.2f}")