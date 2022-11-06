def film_fee(film_budget, people_count, clothes_price_per_person, film_set_price, have_discount_for_more_people, discount_amount):
    people_clothes_price = people_count * clothes_price_per_person
    if people_count > have_discount_for_more_people:
        people_clothes_price = people_clothes_price * discount_amount

    total_fee = people_clothes_price + film_set_price
    money_difference = film_budget - total_fee
    if money_difference >= 0:
        return f'Action!\nWingard starts filming with {money_difference:.2f} leva left.'
    else:
        return f'Not enough money!\nWingard needs {abs(money_difference):.2f} leva more.'


film_budget = float(input())
people_count = int(input())
clothes_price_per_person = float(input())
film_set_price = film_budget * 0.1
have_discount_for_more_people = 150
discount_amount = 0.9


print(film_fee(film_budget, people_count, clothes_price_per_person, film_set_price, have_discount_for_more_people, discount_amount))
