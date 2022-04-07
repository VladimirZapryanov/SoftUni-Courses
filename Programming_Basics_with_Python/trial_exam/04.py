started_people = int(input())
count_stops = int(input())

for stop in range(1, count_stops + 1):
    people_leave = int(input())
    people_enter = int(input())
    if stop % 2 == 1:
        started_people += 2
    elif stop % 2 == 0:
        started_people -= 2
    started_people = (started_people - people_leave) + people_enter

print(f'The final number of passengers is : {started_people}')