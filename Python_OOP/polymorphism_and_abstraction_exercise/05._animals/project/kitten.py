from project.cat import Cat


class Kitten(Cat):
    sound = "Meow"

    def __init__(self, name, age):
        super().__init__(name, age, gender="Female")


