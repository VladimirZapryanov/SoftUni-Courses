easter_bread_numbers = int(input())
eggs_box_numbers = int(input())
cookies_numbers = int(input())

eggs_in_box = 12
easter_bread_price = 3.20
eggs_box_price = 4.35
cookies_price = 5.40
egg_paint_price = 0.15

all_eggs_price = eggs_box_price * eggs_box_numbers
all_easter_bread_price = easter_bread_price * easter_bread_numbers
all_cookies_price = cookies_price * cookies_numbers
all_eggs_paint_price = eggs_box_numbers * eggs_in_box * egg_paint_price
all_cost = all_eggs_paint_price + all_eggs_price + all_easter_bread_price + all_cookies_price

print(f'{all_cost:.2f}')