"""Zaimplementowano klasę o nazwie Circle. Do klasy dodaj właściwość o nazwie area (tylko do odczytu), która będzie obliczać pole koła o zadanym promieniu radius. Właściwość area ma być wyliczana tylko przy pierwszym odczycie lub po modyfikacji atrybutu radius. W tym celu należy zmodyfikować także sposób ustawiania wartości atrybutu radius w metodzie __init__(). Należy upewnić się, że po zmianie atrybutu radius wartość atrybutu area jest przeliczana na nowo.



Następnie utwórz instancję klasy o nazwie circle i promieniu 3. W odpowiedzi wyświetl wartość atrybutu area w przybliżeniu do czterech miejsc po przecinku do konsoli.



Oczekiwany wynik:



28.2743"""

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius * self._radius
        return self._area


circle = Circle(3)
print(f'{circle.area:.4f}')
