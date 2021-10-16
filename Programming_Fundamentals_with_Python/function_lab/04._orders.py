def total_price(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1.00
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2.00


order = input()
value = int(input())
total_value = total_price(order, value)
print(f"{total_value:.2f}")


