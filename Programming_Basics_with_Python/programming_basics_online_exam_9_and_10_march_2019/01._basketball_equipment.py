year_fee = int(input())

sneakers_price = year_fee * 0.6
outfit_price = sneakers_price * 0.8
ball_price = outfit_price / 4
accessories_price = ball_price / 5

total_fee = year_fee + sneakers_price + outfit_price + ball_price + accessories_price

print(f'{total_fee:.2f}')