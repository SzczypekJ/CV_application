"""Podana jest poniższa klasa Point. Zaimplementuj metodę calc_distance(), która policzy odległość dwóch punktów na płaszczyźnie. Następnie utwórz dwie instancje klasy Point o współrzędnych (0, 3) oraz (4, 0) i policz odległość tych punktów (wywołaj metodę calc_distance()).



Oczekiwany wynik:



5.0"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def reset(self):
        self.x = 0
        self.y = 0

    def calc_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


point1 = Point(0, 3)
point2 = Point(4, 0)
print(point1.calc_distance(point2))
