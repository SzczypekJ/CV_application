"""Zaimplementowano klasę o nazwie Laptop, która w metodzie __init__() ustawia wartość atrybutu chronionego _price przechowującego cenę laptopa (na razie bez żadnej walidacji). Następnie zaimplementowano metodę do odczytywania tego atrybutu o nazwie get_price(). Zaimplementuj metodę do modyfikacji tego atrybutu o nazwie set_price(), która dokona walidacji ustawianej wartości. Walidacja sprawdza:

czy ustawiana wartość jest obiektem typu int lub float, jeśli nie podnosi błąd TypeError o treści:


'The price attribute must be an int or float type.'


kolejno czy ustawiana wartość jest dodatnia, jeśli nie podnosi błąd ValueError o treści:


'The price attribute must be a positive int or float value.'


Następnie utwórz instancję klasy Laptop z ceną 3499 i wykorzystując metodę set_price() spróbuj ustawić cenę na wartość tekstową '-3000'. Jeżeli zostanie podniesiony błąd wydrukuj do konsoli komunikat o błędzie. Użyj klauzuli try... except... w rozwiązaniu.



Oczekiwany wynik:



The price attribute must be an int or float type."""


class Laptop:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if isinstance(value, (int, float)):
            if self._price > 0:
                self._price = value
            else:
                raise ValueError(
                    'The price attribute must be a positive int or float value.')
        else:
            raise TypeError(
                'The price attribute must be an int or float type.')


laptop = Laptop(3499)
try:
    laptop.set_price('-3000')
except TypeError as error:
    print(error)
