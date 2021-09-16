month = input()
overnight = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if overnight > 14:
        studio = studio - studio * 0.30
        apartment = apartment - apartment * 0.10
    elif overnight > 7:
        studio = studio - studio * 0.05
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if overnight > 14:
        studio = studio - studio * 0.20
        apartment = apartment - apartment * 0.10
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if overnight > 14:
        apartment = apartment - apartment * 0.10

print(f"Apartment: {overnight * apartment:.2f} lv.")
print(f"Studio: {overnight * studio:.2f} lv.")