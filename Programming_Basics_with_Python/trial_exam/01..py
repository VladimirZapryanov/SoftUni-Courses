<<<<<<< HEAD
import math
speed = float(input())
petrol = float(input())
distance = 384400 * 2
needed_time = distance / speed
all_time = needed_time + 3
needed_petrol = (petrol * distance) / 100
print(math.ceil(all_time))
=======
import math
speed = float(input())
petrol = float(input())
distance = 384400 * 2
needed_time = distance / speed
all_time = needed_time + 3
needed_petrol = (petrol * distance) / 100
print(math.ceil(all_time))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
print(round(needed_petrol))