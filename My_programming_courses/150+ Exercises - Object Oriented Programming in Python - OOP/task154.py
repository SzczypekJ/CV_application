"""Podana jest implementacja klas: Product oraz Warehouse. Do klasy Warehouse dodaj metodę o nazwie add_product() pozwalającą dodać instancję klasy Product do listy products (atrybut klasy Warehouse). Jeżeli nazwa produktu znajduje się już w liście products pomiń dodawanie produktu.



Następnie utwórz instancję klasy Warehouse o nazwie warehouse. Wykorzystując metodę add_product() dodaj poniższe produkty:

'Laptop', 3900.0

'Mobile Phone', 1990.0

'Mobile Phone', 1990.0



Zauważ, że drugi i trzeci produkt to duplikat. Metoda add_product() powinna zapobiec dodawania duplikatów. Następnie wydrukuj do konsoli wartość atrybutu products instancji warehouse.



Oczekiwany wynik:



[Product(product_name='Laptop', price=3900.0), Product(product_name='Mobile Phone', price=1990.0)]"""

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

    def add_product(self, product_name, price):
        product_names = [
            product.product_name for product in self.products
        ]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))


warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Mobile Phone', 1990.0)
print(warehouse.products)
