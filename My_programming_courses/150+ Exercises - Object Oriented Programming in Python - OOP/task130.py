"""Utwórz klasę abstrakcyjną o nazwie Figure wraz z metodą abstrakcyjną area. Następnie utwórz klasę Square dziedziczącą po klasie Figure, która w konstruktorze przyjmie długość boku kwadratu i zaimplementuje metodę area() pozwalającą na wyliczenie pola kwadratu o zadanym boku.



Następnie spróbuj utworzyć instancję klasy Figure w przypadku błędu wydrukuj komunikat o błędzie do konsoli.



Oczekiwany wynik:



Can't instantiate abstract class Figure with abstract methods area"""

from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Figure):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


try:
    obj = Figure()
except TypeError as error:
    print(error)
