"""Zaimplementowano klasę o nazwie Laptop, która w metodzie __init__() ustawia wartość atrybutu chronionego _price przechowującego cenę laptopa (na razie bez żadnej walidacji). Następnie zaimplementowano metodę do odczytywania tego atrybutu o nazwie get_price() oraz metodę do modyfikacji tego atrybutu o nazwie set_price().



Dodaj walidację atrybutu _price także na etapie tworzenia instancji (metoda __init__()). Następnie spróbuj utworzyć instancję klasy Laptop z ujemną ceną tj. -3499. Jeżeli zostanie podniesiony błąd wydrukuj do konsoli komunikat o błędzie.



Oczekiwany wynik:



The price attribute must be a positive int or float value."""


class Laptop:
    def __init__(self, price):
        #  solution 1  - worst than 2 solution because we have a method to validate our value - set_price()
        # if not isinstance(price, (int, float)):
        #     raise TypeError(
        #         'The price attribute must be an int or float type.')

        # if not price > 0:
        #     raise ValueError('The price attribute must be a positive int or '
        #                      'float value.')

        # self._price = price
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, value):

        if not isinstance(value, (int, float)):
            raise TypeError(
                'The price attribute must be an int or float type.')

        if not value > 0:
            raise ValueError('The price attribute must be a positive int or '
                             'float value.')

        self._price = value


try:
    laptop = Laptop(-3499)
except ValueError as error:
    print(error)
