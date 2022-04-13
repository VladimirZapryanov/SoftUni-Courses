<<<<<<< HEAD
class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        if self.status() >= amount:
            self.quantity += amount

    def status(self):
        return self.size - self.quantity


"""
some test:
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
"""

=======
class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        if self.status() >= amount:
            self.quantity += amount

    def status(self):
        return self.size - self.quantity


"""
some test:
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
"""

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
