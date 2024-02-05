"""Podana jest implementacja klasy Product. Zaimplementuj klasę o nazwie Warehouse, która w metodzie __init__() ustawi atrybut instancji klasy Warehouse o nazwie products na pustą listę.



Następnie utwórz instancję klasy Warehouse o nazwie warehouse i wyświetl wartość atrybutu products do konsoli.



Oczekiwany wynik:



[]"""

import uuid


class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


class Warehouse:
    def __init__(self):
        self.products = []


warehouse = Warehouse()
print(warehouse.products)
