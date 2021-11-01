orders = {}
while True:
    command = input()
    if command == "buy":
        break
    product, price, quantity = command.split()
    if product not in orders:
        orders[product] = []
        orders[product].append(float(price))
        orders[product].append(int(quantity))
    else:
        values = orders.get(product)
        if values[0] != float(price):
            values[0] = float(price)
        values[1] += int(quantity)
for key, value in orders.items():
    print(f"{key} -> {value[1] * value[0]:.2f}")