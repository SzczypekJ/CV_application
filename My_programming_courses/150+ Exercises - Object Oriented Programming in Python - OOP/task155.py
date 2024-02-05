"""Podana jest implementacja klas: Product oraz Warehouse. Do klasy Warehouse dodaj metodę o nazwie remove_product() pozwalającą usunąć instancję klasy Product z listy products (atrybut klasy Warehouse) o zadanej nazwie produktu. Jeżeli nazwa produktu nie znajduje się na liście products nie wykonuj niczego.



Następnie utwórz instancję klasy Warehouse o nazwie warehouse. Wykorzystując metodę add_product() dodaj poniższe produkty:

'Laptop', 3900.0

'Mobile Phone', 1990.0

'Camera', 2900.0



Kolejno wykorzystując metodę remove_product() usuń produkt o nazwie 'Mobile Phone'.



W odpowiedzi wydrukuj do konsoli wartość atrybutu products instancji warehouse.



Oczekiwany wynik:



[Product(product_name='Laptop', price=3900.0), Product(product_name='Camera', price=2900.0)]
"""
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
        product_names = [product.product_name for product in self.products]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name):
        for product in self.products:
            if product_name == product.product_name:
                self.products.remove(product)


warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.remove_product('Mobile Phone')
print(warehouse.products)
