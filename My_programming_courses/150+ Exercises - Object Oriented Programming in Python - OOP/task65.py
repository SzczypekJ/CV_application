"""Zaimplementowano klasę o nazwie Laptop, która w metodzie __init__() ustawia wartość atrybutu chronionego _price przechowującego cenę laptopa (na razie bez żadnej walidacji). Następnie zaimplementowano metodę do odczytywania tego atrybutu o nazwie get_price() oraz metodę do modyfikacji tego atrybutu o nazwie set_price().



Utwórz instancję klasy Laptop z ceną 3499 i wykorzystując metodę set_price() spróbuj ustawić cenę na wartość  -3000. Jeżeli zostanie podniesiony błąd wydrukuj do konsoli komunikat o błędzie. Użyj klauzuli try... except... w rozwiązaniu.



Oczekiwany wynik:



The price attribute must be a positive int or float value."""


class Laptop:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if isinstance(value, (int, float)):
            if value > 0:
                self._price = value
            else:
                raise ValueError(
                    'The price attribute must be a positive int '
                    'or float value.'
                )
        else:
            raise TypeError(
                'The price attribute must be an int or float type.'
            )


laptop = Laptop(3499)
try:
    laptop.set_price(-3000)
except ValueError as error:
    print(error)
