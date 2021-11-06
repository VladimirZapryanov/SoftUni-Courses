class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return self.radius * self.radius * self.pi

    def get_circumference(self):
        return 2 * self.radius * self.pi


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

