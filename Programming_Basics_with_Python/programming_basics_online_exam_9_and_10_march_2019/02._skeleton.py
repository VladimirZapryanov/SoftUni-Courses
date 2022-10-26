control_minutes = int(input())
control_seconds = int(input())
chute_meters = float(input())
seconds_for_100_meters = int(input())

control_seconds = control_seconds + control_minutes * 60
reduced_time = chute_meters / 120
total_reduced_time = reduced_time * 2.5
marin_time = (chute_meters / 100) * seconds_for_100_meters - total_reduced_time

if marin_time <= control_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {marin_time:.3f}.')
else:
    time_difference = marin_time - control_seconds
    print(f'No, Marin failed! He was {time_difference:.3f} second slower.')