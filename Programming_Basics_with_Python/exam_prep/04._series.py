budget = float(input())
count_series = int(input())
spend_money = 0
for serial in range(1, count_series + 1):
    name = input()
    price = float(input())
    if name == "Thrones":
        price = price - 0.50 * price
    elif name == "Lucifer":
        price = price - 0.40 * price
    elif name == "Protector":
        price = price - 0.3 * price
    elif name == "TotalDrama":
        price = price - 0.20 * price
    elif name == "Area":
        price = price - 0.10 * price
    spend_money += price
if budget >= spend_money:
    left_money = budget - spend_money
    print(f"You bought all the series and left with {left_money:.2f} lv.")
else:
    need_money = spend_money - budget
    print(f"You need {need_money:.2f} lv. more to buy the series!")




