"""Podana jest implementacja klas Figure oraz Square. Do klasy Figure dodaj metodę abstrakcyjną o nazwie perimeter(), następnie zaimplementuj ją w klasie Square. Metoda perimeter() powinna zwracać obwód kwadratu.



Kolejno utwórz instancję klasy Square o boku 10 i wykorzystując metody area() oraz perimeter() wyświetl pole i obwód tak utworzonej instancji do konsoli.



Oczekiwany wynik:



100
40
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return self.a * 4


obj = Square(10)
print(obj.area())
print(obj.perimeter())
