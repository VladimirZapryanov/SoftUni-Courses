hour_of_day = int(input())
day_of_week = input()
if 10 <= hour_of_day <= 18 and (day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" \
    or day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday"):
    print("open")
else:
    print("closed")
