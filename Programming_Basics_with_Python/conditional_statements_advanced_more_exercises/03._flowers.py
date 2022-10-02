chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()

chrysanthemums_price_summer = 2.00
roses_price_summer = 4.10
tulips_price_summer = 2.50

chrysanthemums_price_winter = 3.75
roses_price_winter = 4.50
tulips_price_winter = 4.15

tulips_discount = 5 / 100
roses_discount = 10 / 100
all_flowers_discount = 20 / 100
price_increase = 15 / 100
arranging_price = 2
flowers_price = 0

if season == 'Spring' or season == 'Summer':
    flowers_price = chrysanthemums_count * chrysanthemums_price_summer + roses_count * roses_price_summer + tulips_count * tulips_price_summer
elif season == 'Autumn' or season == 'Winter':
    flowers_price = chrysanthemums_count * chrysanthemums_price_winter + roses_count * roses_price_winter + tulips_count * tulips_price_winter

if is_holiday == 'Y':
    flowers_price = flowers_price + (flowers_price * price_increase)

if tulips_count >= 7 and season == 'Spring':
    flowers_price = flowers_price - (flowers_price * tulips_discount)

if roses_count >= 10 and season == 'Winter':
    flowers_price = flowers_price - (flowers_price * roses_discount)

all_flowers_count = chrysanthemums_count + roses_count + tulips_count
if all_flowers_count >= 20:
    flowers_price = flowers_price - (flowers_price * all_flowers_discount)

flowers_price += arranging_price

print(f'{flowers_price:.2f}')
