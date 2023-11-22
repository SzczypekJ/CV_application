class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_the_surface_area(self):
        surface_area = self.a * self.b
        return surface_area


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Cube():
    def __init__(self, square: Square):
        self.square = square
        self.a = square.a

    def calculate_the_surface_area(self):
        return self.square.calculate_the_surface_area() * 6

    def calculate_the_volume(self):
        return self.square.calculate_the_surface_area() * self.a


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_volume(self):
        return self.base.calculate_the_surface_area() * self.height

    def count_surface_area(self):
        return 2 * self.base.calculate_the_surface_area() + 2 * self.base.a * self.height + 2 * self.base.b * self.height
