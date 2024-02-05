"""Podana jest poniższa klasa Point. Zaimplementuj metodę reset(), która pozwoli ustawić wartości atrybutów x oraz y na zero. Następnie utwórz instancję klasy Point o współrzędnych (4, 2) i wydrukuj ją do konsoli. Wywołaj metodę reset() i jeszcze raz wydrukuj instancję do konsoli.



Oczekiwany wynik:



Point(x=4, y=2)
Point(x=0, y=0)"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def reset(self):
        self.x = 0
        self.y = 0


point = Point(4, 2)
print(point)
point.reset()
print(point)
