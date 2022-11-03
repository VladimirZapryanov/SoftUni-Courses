from math import ceil

easter_breads = int(input())
sugar_packet_grams = 950
flour_packet_grams = 750

total_sugar_amount = 0
total_flour_amount = 0
max_amount_of_sugar = 0
max_amount_of_flour = 0
for _ in range(easter_breads):
    current_sugar_amount = int(input())
    current_flour_amount = int(input())

    total_sugar_amount += current_sugar_amount
    total_flour_amount += current_flour_amount

    if current_sugar_amount > max_amount_of_sugar:
        max_amount_of_sugar = current_sugar_amount
    if current_flour_amount > max_amount_of_flour:
        max_amount_of_flour = current_flour_amount

needed_sugar_packages = ceil(total_sugar_amount / sugar_packet_grams)
needed_flour_packages = ceil(total_flour_amount / flour_packet_grams)

print(f'Sugar: {needed_sugar_packages}')
print(f'Flour: {needed_flour_packages}')
print(f'Max used flour is {max_amount_of_flour} grams, max used sugar is {max_amount_of_sugar} grams.')