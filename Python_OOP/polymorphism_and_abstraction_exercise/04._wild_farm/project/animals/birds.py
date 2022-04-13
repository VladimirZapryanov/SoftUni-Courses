<<<<<<< HEAD
from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOODS = ["Vegetable", "Fruit", "Meat", "Seed"]
    WEIGHT_MULTIPLIER = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"


=======
from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOODS = ["Vegetable", "Fruit", "Meat", "Seed"]
    WEIGHT_MULTIPLIER = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"


>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
