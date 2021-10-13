command = input()

dict_product = {}

while not command == "statistics":
    product, quantity = command.split(": ")
    if product not in dict_product:
        dict_product[product] = int(quantity)
    else:
        dict_product[product] += int(quantity)
    command = input()

print("Products in stock:")

for product, quantity in dict_product.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(dict_product)}")
print(f"Total Quantity: {sum(dict_product.values())}")

