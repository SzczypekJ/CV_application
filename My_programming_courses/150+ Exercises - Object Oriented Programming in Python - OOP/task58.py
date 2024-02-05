"""Zaimplementowano klasę o nazwie Laptop, która przy tworzeniu instancji ustawia poniższe atrybuty instancji:

brand

model

price



Przy tworzeniu instancji dodano walidację dla atrybutu price. Spróbuj utworzyć instancję o nazwie laptop klasy Laptop o podanych wartościach atrybutów:

brand = 'Acer'

model = 'Predator'

price = '5900'



Zauważ, że w tym przypadku wartość atrybutu price przekazywana jest jako obiekt typu str. W przypadku błędu, wydrukuj komunikat o błędzie do konsoli (użyj klauzuli try... except...)



Oczekiwany wynik:



The price attribute must be a positive int or float."""


from typing import Type


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else:
            raise TypeError(
                'The price attribute must be a positive int or float.')


try:
    laptop = Laptop("Acer", "Predator", "5900")
except TypeError as error:
    print(error)
