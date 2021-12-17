budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price + (flour_price * 0.25)
recipe_milk_price = milk_price / 4
cozonacs_price = flour_price + eggs_price + recipe_milk_price
colored_eggs = 0
left_budget = budget
cozonacs = 0

while left_budget >= cozonacs_price:
    colored_eggs += 3
    cozonacs += 1
    left_budget -= cozonacs_price
    if cozonacs % 3 == 0 :
        colored_eggs -= cozonacs - 2

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {left_budget:.2f}BGN left.")





