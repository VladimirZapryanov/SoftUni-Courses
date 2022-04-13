<<<<<<< HEAD
from project.animal import Animal


class Dog(Animal):
    sound = "Woof!"

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

=======
from project.animal import Animal


class Dog(Animal):
    sound = "Woof!"

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
