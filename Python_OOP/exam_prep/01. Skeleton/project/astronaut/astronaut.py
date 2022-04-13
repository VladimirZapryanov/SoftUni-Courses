<<<<<<< HEAD
from abc import ABC, abstractmethod


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = value.strip()
        if value == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount):
        self.oxygen += amount

    def __str__(self):
        result = f'Name: {self.name}' + '\n'
        result += f'Oxygen: {self.oxygen}' + '\n'
        result += f"Backpack items: {', '.join(self.backpack) if len(self.backpack) > 0 else 'none'}"

=======
from abc import ABC, abstractmethod


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = value.strip()
        if value == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount):
        self.oxygen += amount

    def __str__(self):
        result = f'Name: {self.name}' + '\n'
        result += f'Oxygen: {self.oxygen}' + '\n'
        result += f"Backpack items: {', '.join(self.backpack) if len(self.backpack) > 0 else 'none'}"

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
        return result