number_of_pages = int(input())
number_of_pages_per_hours = int(input())
number_of_days = int(input())
hours_needed_for_all_book = number_of_pages / number_of_pages_per_hours
reading_hours_per_day = hours_needed_for_all_book / number_of_days
print(reading_hours_per_day)
