<<<<<<< HEAD
from project.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters

=======
from project.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
