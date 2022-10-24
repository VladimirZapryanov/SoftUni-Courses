time_for_picture = int(input())
numbers_of_scenes = int(input())
time_per_scene = int(input())

time_for_picture = time_for_picture * 0.85
needed_time = numbers_of_scenes * time_per_scene
time_difference = time_for_picture - needed_time

if time_for_picture >= needed_time:
    print(f'You managed to finish the movie on time! You have {round(time_difference)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(abs(time_difference))} minutes.')