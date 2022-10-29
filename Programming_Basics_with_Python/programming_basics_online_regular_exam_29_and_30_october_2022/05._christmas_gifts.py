command = input()

toy_price = 5
sweater_price = 15
kids_count = 0
adult_count = 0

while not command == 'Christmas':
    years = int(command)

    if years <= 16:
        kids_count += 1
    elif years > 16:
        adult_count += 1

    command = input()

toys_cost = toy_price * kids_count
sweaters_cost = sweater_price * adult_count
print(f'Number of adults: {adult_count}')
print(f'Number of kids: {kids_count}')
print(f'Money for toys: {toys_cost}')
print(f'Money for sweaters: {sweaters_cost}')