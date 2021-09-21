import math
time_one = int(input())
time_two = int(input())
time_three = int(input())
total_time = time_one + time_two + time_three
minutes = total_time / 60
seconds = total_time % 60
minutes = math.floor(minutes)
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
