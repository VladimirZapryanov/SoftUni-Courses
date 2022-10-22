wrapping_paper_numbers = int(input())
fabric_numbers = int(input())
litters_of_glue = float(input())
discount_percent = int(input())

wrapping_paper_price = 5.80
fabric_price = 7.20
glue_price = 1.20

needed_money = wrapping_paper_numbers * wrapping_paper_price + fabric_numbers * fabric_price + litters_of_glue * glue_price
total_needed_money = needed_money - (needed_money * discount_percent / 100)

print(f'{total_needed_money:.3f}')

