length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percent_occupied_value = float(input())
liters_fish_tank = (length_in_cm * width_in_cm * height_in_cm) * 0.001
water_value = liters_fish_tank - (liters_fish_tank * percent_occupied_value / 100)
print(water_value)