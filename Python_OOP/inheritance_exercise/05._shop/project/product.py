<<<<<<< HEAD
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity

    def increase(self, quantity):
        self.quantity += quantity

    def __repr__(self):
        return self.name




=======
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity

    def increase(self, quantity):
        self.quantity += quantity

    def __repr__(self):
        return self.name




>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
