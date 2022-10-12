last_sector = input()
first_sector_rows = int(input())
odd_row_seats = int(input())

first_sector_number = ord('A')
last_sector_number = ord(last_sector)
even_row_seats = odd_row_seats + 2
total_seats = 0

for sector in range(first_sector_number, last_sector_number + 1):
    first_sector_rows += 1
    for row in range(1, first_sector_rows):
        if row % 2 == 1:
            for seat in range(1, odd_row_seats + 1):
                total_seats += 1
                print(f'{chr(sector)}{row}{chr(96 + seat)}')
        else:
            for seat in range(1, even_row_seats + 1):
                print(f'{chr(sector)}{row}{chr(96 + seat)}')
                total_seats += 1

print(total_seats)