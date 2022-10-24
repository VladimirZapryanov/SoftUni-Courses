from math import floor

movie_name = input()
season_number = int(input())
episode_number = int(input())
episode_time = float(input())

episode_time_with_advertising = episode_time * 1.2
final_episode_more_time = season_number * 10
needed_time = season_number * episode_number * episode_time_with_advertising + final_episode_more_time

print(f'Total time needed to watch the {movie_name} series is {floor(needed_time)} minutes.')