t_shirt_price = float(input())
win_price = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.2
soccer_cleats_price = (t_shirt_price + shorts_price) * 2

equipment_price = t_shirt_price + shorts_price + socks_price + soccer_cleats_price
total_equipment_price = equipment_price * 0.85

if total_equipment_price >= win_price:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_equipment_price:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {win_price - total_equipment_price:.2f} lv. more.')