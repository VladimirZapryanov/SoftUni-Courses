movie_name = input()
type_hall = input()
count_tickets = int(input())
price_per_ticket = 0
if movie_name == "A Star Is Born":
    if type_hall == "normal":
        price_per_ticket = 7.50
    if type_hall == "luxury":
        price_per_ticket = 10.50
    if type_hall == "ultra luxury":
        price_per_ticket = 13.50
elif movie_name == "Bohemian Rhapsody":
    if type_hall == "normal":
        price_per_ticket = 7.35
    if type_hall == "luxury":
        price_per_ticket = 9.45
    if type_hall == "ultra luxury":
        price_per_ticket = 12.75
elif movie_name == "Green Book":
    if type_hall == "normal":
        price_per_ticket = 8.15
    if type_hall == "luxury":
        price_per_ticket = 10.25
    if type_hall == "ultra luxury":
        price_per_ticket = 13.25
elif movie_name == "The Favourite":
    if type_hall == "normal":
        price_per_ticket = 8.75
    if type_hall == "luxury":
        price_per_ticket = 11.55
    if type_hall == "ultra luxury":
        price_per_ticket = 13.95
profit = count_tickets * price_per_ticket
print(f"{movie_name} -> {profit:.2f} lv.")