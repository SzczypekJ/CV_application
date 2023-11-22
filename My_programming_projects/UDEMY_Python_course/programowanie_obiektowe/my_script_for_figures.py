from figures import Rectangle, Square, Cube, Cuboid

rectangle = Rectangle(2, 5)
square = Square(3)
cube = Cube(Square(3))
cuboid = Cuboid(Rectangle(2, 3), 4)

# print(cuboid.count_volume())

# print(cube.a)

# print(rectangle.calculate_the_surface_area())

# print(square.calculate_the_surface_area())

print(cube.calculate_the_surface_area())
print(cube.calculate_the_volume())
print(cuboid.count_surface_area())
