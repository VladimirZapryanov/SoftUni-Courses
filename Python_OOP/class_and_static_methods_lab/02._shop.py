<<<<<<< HEAD
class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type, capacity=10):
        return cls(name, type, capacity)

    def add_item(self, item_name):
        if self.capacity <= 0:
            return "Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 1
            self.capacity -= 1
            return f"{item_name} added to the shop"
        self.items[item_name] += 1
        self.capacity -= 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        self.capacity += amount
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)
print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))
print(fresh_shop.remove_item("Bananas", 1))
print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
=======
class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type, capacity=10):
        return cls(name, type, capacity)

    def add_item(self, item_name):
        if self.capacity <= 0:
            return "Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 1
            self.capacity -= 1
            return f"{item_name} added to the shop"
        self.items[item_name] += 1
        self.capacity -= 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        self.capacity += amount
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)
print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))
print(fresh_shop.remove_item("Bananas", 1))
print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
