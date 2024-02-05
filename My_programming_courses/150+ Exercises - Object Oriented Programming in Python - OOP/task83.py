"""Zaimplementuj klasę o nazwie Rectangle, która będzie posiadać dwa atrybuty instancji o nazwach:

width (do odczytu i modyfikacji)

height (do odczytu i modyfikacji)



Dodaj także atrybut o nazwie area, która będzie przechowywać pole prostokąta o zadanych bokach (tylko do odczytu). Właściwość area ma być wyliczana tylko przy pierwszym odczycie lub po modyfikacji dowolnego z boków prostokąta. Pomiń walidację ustawianych wartości atrybutów.



Następnie utwórz instancję o nazwie rectangle o szerokości 3 oraz wysokości 4 i wydrukuj do konsoli informację o instancji rectangle tak jak pokazano poniżej:



width: 3, height: 4 -> area: 12"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._area = None

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value
        self._area = None

    @height.setter
    def height(self, value):
        self._height = value
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = self._height * self._width
        return self._area


rectangle = Rectangle(3, 4)
print(
    f"width: {rectangle.width}, height: {rectangle.height} -> area: {rectangle.area}")
