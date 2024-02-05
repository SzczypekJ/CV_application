"""Zaimplementuj klasę o nazwie Laptop, która w metodzie __init__() ustawi wartość atrybutu chronionego _price przechowującego cenę laptopa (na razie bez żadnej walidacji). Następnie zaimplementuj metodę do odczytywania tego atrybutu o nazwie get_price() oraz metodę do modyfikacji tego atrybutu o nazwie set_price() również bez walidacji.



Następnie utwórz instancję klasy Laptop z ceną 3499 i wykonaj następujące kroki:

wykorzystując metodę get_price() wydrukuj wartość atrybutu chronionego _price do konsoli

wykorzystując metodę set_price() ustaw wartość atrybutu chronionego _price na 3999

wykorzystując metodę get_price() ponownie wydrukuj wartość atrybutu chronionego _price do konsoli



Oczekiwany wynik:



3499
3999"""


class Laptop:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        # solution 1
        # for attr in self.__dict__:
        #     print(self.__dict__[attr])
        # solution 2
        print(self._price)


    def set_price(self, value):
        self._price = value


laptop = Laptop(3499)
laptop.get_price()
laptop.set_price(3999)
laptop.get_price()
