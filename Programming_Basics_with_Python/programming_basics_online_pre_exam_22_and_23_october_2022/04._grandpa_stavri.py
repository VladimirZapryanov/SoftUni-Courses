num_of_days = int(input())
liter_counter = 0
degrees_counter = 0
for everyday in range(1, num_of_days + 1):
    liters = float(input())
    liter_counter += liters
    degrees = float(input())
    degrees_counter += degrees * liters
final_degrees = degrees_counter / liter_counter
print(f"Liter: {liter_counter:.2f}")
print(f"Degrees: {final_degrees:.2f}")
if final_degrees <= 38:
    print("Not good, you should baking!")
elif 42 >= final_degrees > 38:
    print("Super!")
elif final_degrees > 42:
    print("Dilution with distilled water!")