def tom_sleep(free_days, year_playing_minutes, work_day_playing_minutes, free_day_playing_minutes, days_in_year):
    work_days = days_in_year - free_days
    total_playing_in_minutes = (work_day_playing_minutes * work_days) + (free_day_playing_minutes * free_days)
    difference_between_hours = year_playing_minutes - total_playing_in_minutes

    if total_playing_in_minutes > year_playing_minutes:
        return f'Tom will run away \n{abs(difference_between_hours) // 60} hours and {abs(difference_between_hours) % 60} minutes more for play'
    else:
        return f'Tom sleeps well \n{difference_between_hours // 60} hours and {difference_between_hours % 60} minutes less for play'


free_days = int(input())

year_playing_minutes = 30000
work_day_playing_minutes = 63
free_day_playing_minutes = 127
days_in_year = 365

print(tom_sleep(free_days, year_playing_minutes, work_day_playing_minutes, free_day_playing_minutes, days_in_year))
