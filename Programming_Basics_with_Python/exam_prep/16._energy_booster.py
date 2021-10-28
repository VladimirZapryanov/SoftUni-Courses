fruit = input()
size = input()
set_count = int(input())

watermelon_s = 56
watermelon_b = 28.70
mango_s = 36.66
mango_b = 19.60
pineapple_s = 42.10
pineapple_b = 24.80
raspberry_s = 20
raspberry_b = 15.20

small_pak_price = 0
big_pak_price = 0
needed_money = 0
total_money = 0

if size == "small":
    if fruit == "Watermelon":
        small_pak_price = 2 * watermelon_s
    elif fruit == "Mango":
        small_pak_price = 2 * mango_s
    elif fruit == "Pineapple":
        small_pak_price = 2 * pineapple_s
    elif fruit == "Raspberry":
        small_pak_price = 2 * raspberry_s

    needed_money = small_pak_price * set_count
    total_money = needed_money

    if 400 <= needed_money <= 1000:
        total_money = needed_money - needed_money * 0.15
    elif needed_money > 1000:
        total_money = needed_money - needed_money * 0.5

elif size == "big":
    if fruit == "Watermelon":
        big_pak_price = 5 * watermelon_b
    elif fruit == "Mango":
        big_pak_price = 5 * mango_b
    elif fruit == "Pineapple":
        big_pak_price = 5 * pineapple_b
    elif fruit == "Raspberry":
        big_pak_price = 2 * raspberry_b

    needed_money = big_pak_price * set_count
    total_money = needed_money

    if 400 <= needed_money <= 1000:
        total_money = needed_money - needed_money * 0.15
    elif needed_money > 1000:
        total_money = needed_money - needed_money * 0.5

print(f"{total_money:.2f} lv.")

