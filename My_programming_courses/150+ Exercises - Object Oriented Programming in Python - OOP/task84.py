"""Zaimplementowano klasę o nazwie Rectangle, która posiada następujące atrybuty instancji:

width (do odczytu i do modyfikacji)

height (do odczytu i do modyfikacji)

area (tylko do odczytu)



Dodaj także właściwość o nazwie perimeter, która będzie przechowywać obwód prostokąta o zadanych bokach (tylko do odczytu). Właściwość perimeter ma być wyliczana tylko przy pierwszym odczycie lub po modyfikacji dowolnego z boków prostokąta. Pomiń walidację ustawianych wartości atrybutów.



Następnie utwórz instancję o nazwie rectangle o szerokości 3 oraz wysokości 4 i wydrukuj do konsoli informację o instancji rectangle tak jak pokazano poniżej:



width: 3, height: 4 -> perimeter: 14"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._area = None
        self._perimeter = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._area = None
        self._perimeter = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._area = None
        self._perimeter = None

    @property
    def area(self):
        if self._area is None:
            self._area = self._width * self._height
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * self._width + 2 * self._height
        return self._perimeter


rectangle = Rectangle(3, 4)
print(
    f"width: {rectangle.width}, height: {rectangle.height} -> perimeter: {rectangle.perimeter}")
