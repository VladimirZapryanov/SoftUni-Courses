from collections import deque


def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    rest_budget = budget
    products = deque()
    bought_products = []
    for k, v in kwargs.items():
        price = float(v[0])
        quantity = int(v[1])
        total_price = quantity * price
        if rest_budget >= total_price:
            rest_budget -= total_price
            products.append(f"You bought {k} for {total_price:.2f} leva.")
    for _ in range(5):
        if len(products) > 0:
            el = products.popleft()
            bought_products.append(el)

    return "\n".join(bought_products)


"""
some test:
print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
"""
