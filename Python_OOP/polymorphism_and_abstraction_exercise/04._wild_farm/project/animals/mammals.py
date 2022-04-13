<<<<<<< HEAD
from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ["Vegetables", "Fruits"]
    WEIGHT_MULTIPLIER = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 0.4

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOODS = ["Vegetable", "Meat"]
    WEIGHT_MULTIPLIER = 0.3

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
=======
from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ["Vegetables", "Fruits"]
    WEIGHT_MULTIPLIER = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 0.4

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOODS = ["Vegetable", "Meat"]
    WEIGHT_MULTIPLIER = 0.3

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
