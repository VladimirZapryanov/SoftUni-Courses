products = input().split(" ")
searched_products = input().split(" ")

products_dict = {}

for p in range(0, len(products), 2):
    key = products[p]
    value = products[p + 1]
    products_dict[key] = int(value)

for products in searched_products:
    if products in products_dict:
        print(f"We have {products_dict[products]} of {products} left")
    else:
        print(f"Sorry, we don't have {products}")





