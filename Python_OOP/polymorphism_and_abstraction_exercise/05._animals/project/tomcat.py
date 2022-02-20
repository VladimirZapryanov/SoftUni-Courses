from project.cat import Cat


class Tomcat(Cat):
    sound = "Hiss"

    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")


