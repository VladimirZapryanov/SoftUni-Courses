age = int(input())
price_laundry = float(input())
price_per_toy = int(input())
count_toys = 0
saved_money = 0
for birthday in range(1, age + 1):
    if birthday % 2 == 1:
        count_toys += 1
    else:
        saved_money += birthday * 5 - 1
total_money = saved_money + (count_toys * price_per_toy)
if total_money >= price_laundry:
    left_money = total_money - price_laundry
    print(f"Yes! {left_money:.2f}")
else:
    need_money = price_laundry - total_money
    print(f"No! {need_money:.2f}")