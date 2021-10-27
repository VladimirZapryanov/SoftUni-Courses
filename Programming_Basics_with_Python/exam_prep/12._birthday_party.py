house_rent = float(input())

tart_price = house_rent * 0.2
drinks_price = tart_price - tart_price * 0.45
animation_price = house_rent / 3

total_price = tart_price + drinks_price + animation_price + house_rent

print(total_price)
