flower_type = input().capitalize()
quantity_of_flowers = int(input())
budget = int(input())

rose = 5
dahlias = 3.8
tulips = 2.8
narcissus = 3
gladiolus = 2.5

price = 0
discount = 0

if flower_type == 'Roses':
    if quantity_of_flowers > 80:
        price = rose * quantity_of_flowers
        discount = price * 0.1
        price = price - discount
    else:
        price = rose * quantity_of_flowers
elif flower_type == 'Dahlias':
    if quantity_of_flowers > 90:
        price = dahlias * quantity_of_flowers
        discount = price * 0.15
        price = price - discount
    else:
        price = dahlias * quantity_of_flowers
elif flower_type == 'Tulips':
    if quantity_of_flowers > 80:
        price = tulips * quantity_of_flowers
        discount = price * 0.15
        price -= discount
    else:
        price = tulips * quantity_of_flowers
elif flower_type == 'Narcissus':
    if quantity_of_flowers < 120:
        price = narcissus * quantity_of_flowers
        discount = price * 0.15
        price += discount
    else:
        price = narcissus * quantity_of_flowers

elif flower_type == 'Gladiolus':
    if quantity_of_flowers < 80:
        price = gladiolus * quantity_of_flowers
        discount = price * 0.20
        price += discount
    else:
        price = gladiolus * quantity_of_flowers
if price > budget:
    print(f"Not enough money, you need {(price - budget):.2f} leva more.")
else:
    print(
        f"Hey, you have a great garden with {quantity_of_flowers} {flower_type} and {(budget - price):.2f} leva left.")
