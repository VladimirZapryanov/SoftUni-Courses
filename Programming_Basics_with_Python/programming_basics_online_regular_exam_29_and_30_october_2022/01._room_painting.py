from math import ceil, floor

paint_cans_numbers = int(input())
wallpaper_rolls_numbers = int(input())
gloves_price = float(input())
brush_price = float(input())

paint_can_price = 21.50
wallpaper_roll_price = 5.20
gloves_numbers = ceil(wallpaper_rolls_numbers * 0.35)
brush_numbers = floor(paint_cans_numbers * 0.48)

all_staff_price = paint_can_price * paint_cans_numbers + wallpaper_roll_price * wallpaper_rolls_numbers + gloves_price * gloves_numbers + brush_price * brush_numbers
delivery_price = all_staff_price / 15

print(f'This delivery will cost {delivery_price:.2f} lv.')
