rent_for_room = int(input())
cake = rent_for_room * 0.2
drinks = cake - (cake * 0.45)
animator = rent_for_room / 3
needed_money = rent_for_room + cake + drinks + animator
print(needed_money)