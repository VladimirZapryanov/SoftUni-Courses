from math import floor

record = float(input())
distance = float(input())
time_per_one_m = float(input())

slowing_time = floor(distance // 50) * 30

george_time = distance * time_per_one_m + slowing_time

if george_time < record:
    print(f"Yes! The new record is {george_time:.2f} seconds.")
else:
    print(f"No! He was {abs(record - george_time):.2f} seconds slower.")