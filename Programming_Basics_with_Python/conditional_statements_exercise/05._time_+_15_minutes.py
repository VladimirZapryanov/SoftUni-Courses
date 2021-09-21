hours = int(input())
minutes = int(input())
minutes += 15
hours += minutes // 60
minutes %= 60
if hours > 23:
    hours -= 24
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")