joinery_count = int(input())
size_of_joinery = input()
kind_of_delivery = input()

is_valid = True
joinery_price = 0
total_price = 0

if joinery_count <= 10:
    is_valid = False
else:
    if size_of_joinery == "90X130" and 60 >= joinery_count > 30:
        joinery_price += (joinery_count * 110) - (joinery_count * 110) * 0.05
    elif size_of_joinery == "90X130" and joinery_count > 60:
        joinery_price += (joinery_count * 110) - (joinery_count * 110) * 0.08
    elif size_of_joinery == "90X130" and joinery_count <= 30:
        joinery_price += joinery_count * 110
    elif size_of_joinery == "100X150" and 80 >= joinery_count > 40:
        joinery_price += (joinery_count * 140) - (joinery_count * 140) * 0.06
    elif size_of_joinery == "100X150" and joinery_count > 80:
        joinery_price += (joinery_count * 140) - (joinery_count * 140) * 0.10
    elif size_of_joinery == "100X150" and joinery_count <= 40:
        joinery_price += joinery_count * 140
    elif size_of_joinery == "130X180" and 50 >= joinery_count > 20:
        joinery_price += (joinery_count * 190) - (joinery_count * 190) * 0.07
    elif size_of_joinery == "130X180" and joinery_count > 50:
        joinery_price += (joinery_count * 190) - (joinery_count * 190) * 0.12
    elif size_of_joinery == "130X180" and joinery_count <= 20:
        joinery_price += joinery_count * 190
    elif size_of_joinery == "200X300" and 50 >= joinery_count > 25:
        joinery_price += (joinery_count * 250) - (joinery_count * 250) * 0.09
    elif size_of_joinery == "200X300" and joinery_count > 50:
        joinery_price += (joinery_count * 250) - (joinery_count * 250) * 0.14
    elif size_of_joinery == "200X300" and joinery_count <= 25:
        joinery_price += joinery_count * 250

if kind_of_delivery == "With delivery":
    total_price += joinery_price + 60
    if joinery_count > 99:
        total_price -= total_price * 0.04
elif kind_of_delivery == "Without delivery":
    total_price = joinery_price
    if joinery_count > 99:
        total_price -= total_price * 0.04

if is_valid:
    print(f"{total_price:.2f} BGN")
else:
    print("Invalid order")


