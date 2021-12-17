current_year = int(input())

while True:
    current_year += 1
    current_year_as_string = str(current_year)
    if len(current_year_as_string) == len(set(current_year_as_string)):
        print(current_year)
        break
