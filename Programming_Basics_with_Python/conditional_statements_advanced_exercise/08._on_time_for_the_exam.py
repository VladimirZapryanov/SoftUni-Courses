hour_of_examine = int(input())
minutes_of_examine = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())
time_of_examine = hour_of_examine * 60 + minutes_of_examine
time_of_arriving = hour_of_arriving * 60 + minutes_of_arriving
if time_of_arriving > time_of_examine:
    print("Late")
elif time_of_examine - 30 <= time_of_arriving <= time_of_examine:
    print("On time")
else:
    print("Early")
if time_of_examine - 60 < time_of_arriving < time_of_examine:
    print(f"{time_of_examine - time_of_arriving} minutes before the start")
elif time_of_arriving <= time_of_examine - 60:
    difference = time_of_examine - time_of_arriving
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours}:{minutes:0>2d} hours before the start")
elif time_of_examine < time_of_arriving < time_of_examine + 60:
    print(f"{time_of_arriving - time_of_examine} minutes after the start")
elif time_of_arriving >= time_of_examine + 60:
    difference = time_of_arriving - time_of_examine
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours}:{minutes:0>2d} hours after the start")