import math
speed = float(input())
petrol = float(input())
distance = 384400 * 2
needed_time = distance / speed
all_time = needed_time + 3
needed_petrol = (petrol * distance) / 100
print(math.ceil(all_time))
print(round(needed_petrol))