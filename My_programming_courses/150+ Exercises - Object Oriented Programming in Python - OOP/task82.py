"""Zaimplementowano klasę o nazwie Circle. Do klasy dodaj właściwość o nazwie perimeter (tylko do odczytu), która będzie obliczać długość okręgu o zadanym promieniu radius. Właściwość perimeter ma być wyliczana tylko przy pierwszym odczycie lub po modyfikacji atrybutu radius. W tym celu należy zmodyfikować także sposób ustawiania wartości atrybutu radius w metodzie __init__(). Należy upewnić się, że po zmianie atrybutu radius wartość atrybutu perimeter jest przeliczana na nowo.



Następnie utwórz instancję klasy o nazwie circle i promieniu 3. W odpowiedzi wyświetl wartość atrybutu perimeter w przybliżeniu do czterech miejsc po przecinku do konsoli.



Oczekiwany wynik:



18.8496"""

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = None
        self._perimeter = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius * self._radius
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = math.pi * 2 * self._radius
        return self._perimeter


circle = Circle(3)
print(f'{circle.perimeter:.4f}')
