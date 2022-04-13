<<<<<<< HEAD
football_team = input()
type_of_souvenirs = input()
count_of_souvenirs = int(input())
price_per_souvenirs = 0
if football_team == "Argentina":
    if type_of_souvenirs == "flags":
        price_per_souvenirs = 3.25
    elif type_of_souvenirs == "caps":
        price_per_souvenirs = 7.20
    elif type_of_souvenirs == "posters":
        price_per_souvenirs = 5.10
    elif type_of_souvenirs == "stickers":
        price_per_souvenirs = 1.25
    else:
        print("Invalid stock!")
elif football_team == "Brazil":
    if type_of_souvenirs == "flags":
        price_per_souvenirs = 4.20
    elif type_of_souvenirs == "caps":
        price_per_souvenirs = 8.50
    elif type_of_souvenirs == "posters":
        price_per_souvenirs = 5.35
    elif type_of_souvenirs == "stickers":
        price_per_souvenirs = 1.20
    else:
        print("Invalid stock!")
elif football_team == "Croatia":
    if type_of_souvenirs == "flags":
        price_per_souvenirs = 2.75
    elif type_of_souvenirs == "caps":
        price_per_souvenirs = 6.90
    elif type_of_souvenirs == "posters":
        price_per_souvenirs = 4.95
    elif type_of_souvenirs == "stickers":
        price_per_souvenirs = 1.10
    else:
        print("Invalid stock!")
elif football_team == "Denmark":
    if type_of_souvenirs == "flags":
        price_per_souvenirs = 3.10
    elif type_of_souvenirs == "caps":
        price_per_souvenirs = 6.50
    elif type_of_souvenirs == "posters":
        price_per_souvenirs = 4.80
    elif type_of_souvenirs == "stickers":
        price_per_souvenirs = 0.90
    else:
        print("Invalid stock!")
if football_team == "Argentina" or football_team == "Brazil" or football_team == "Croatia" or \
    football_team == "Denmark" and type_of_souvenirs == "flags" or type_of_souvenirs == "caps" or \
    type_of_souvenirs == "posters" or type_of_souvenirs == "stickers":
    print(f"Pepi bought {count_of_souvenirs} {type_of_souvenirs} of {football_team} for {price_per_souvenirs * count_of_souvenirs:.2f} lv.")
elif football_team != "Argentina" or football_team != "Brazil" or football_team != "Croatia" or \
    football_team != "Denmark":
    print("Invalid country!")
elif type_of_souvenirs != "flags" or type_of_souvenirs != "caps" or \
    type_of_souvenirs != "posters" or type_of_souvenirs != "stickers":
    print("Invalid stock!")


=======
football_team = input()
type_of_souvenirs = input()
count_of_souvenirs = int(input())
price_per_souvenirs = 0
if football_team == "Argentina":
    if type_of_souvenirs == "flags":
        price_per_souvenirs = 3.25
    elif type_of_souvenirs == "caps":
        price_per_souvenirs = 7.20
    elif type_of_souvenirs == "posters":
        price_per_souvenirs = 5.10
    elif type_of_souvenirs == "stickers":
        price_per_souvenirs = 1.25
    else:
        print("Invalid stock!")
elif football_team == "Brazil":
    if type_of_souvenirs == "flags":
        price_per_souvenirs = 4.20
    elif type_of_souvenirs == "caps":
        price_per_souvenirs = 8.50
    elif type_of_souvenirs == "posters":
        price_per_souvenirs = 5.35
    elif type_of_souvenirs == "stickers":
        price_per_souvenirs = 1.20
    else:
        print("Invalid stock!")
elif football_team == "Croatia":
    if type_of_souvenirs == "flags":
        price_per_souvenirs = 2.75
    elif type_of_souvenirs == "caps":
        price_per_souvenirs = 6.90
    elif type_of_souvenirs == "posters":
        price_per_souvenirs = 4.95
    elif type_of_souvenirs == "stickers":
        price_per_souvenirs = 1.10
    else:
        print("Invalid stock!")
elif football_team == "Denmark":
    if type_of_souvenirs == "flags":
        price_per_souvenirs = 3.10
    elif type_of_souvenirs == "caps":
        price_per_souvenirs = 6.50
    elif type_of_souvenirs == "posters":
        price_per_souvenirs = 4.80
    elif type_of_souvenirs == "stickers":
        price_per_souvenirs = 0.90
    else:
        print("Invalid stock!")
if football_team == "Argentina" or football_team == "Brazil" or football_team == "Croatia" or \
    football_team == "Denmark" and type_of_souvenirs == "flags" or type_of_souvenirs == "caps" or \
    type_of_souvenirs == "posters" or type_of_souvenirs == "stickers":
    print(f"Pepi bought {count_of_souvenirs} {type_of_souvenirs} of {football_team} for {price_per_souvenirs * count_of_souvenirs:.2f} lv.")
elif football_team != "Argentina" or football_team != "Brazil" or football_team != "Croatia" or \
    football_team != "Denmark":
    print("Invalid country!")
elif type_of_souvenirs != "flags" or type_of_souvenirs != "caps" or \
    type_of_souvenirs != "posters" or type_of_souvenirs != "stickers":
    print("Invalid stock!")


>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
