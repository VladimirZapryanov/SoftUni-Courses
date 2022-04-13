<<<<<<< HEAD
from abc import ABC, abstractmethod


class Animal(ABC):
    sound = ""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        pass

    def make_sound(self):
        return self.sound

=======
from abc import ABC, abstractmethod


class Animal(ABC):
    sound = ""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        pass

    def make_sound(self):
        return self.sound

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
