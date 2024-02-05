"""Podana jest implementacja klas: Product oraz Warehouse. Do klasy Product dodaj metodę __str__() będącą nieformalną reprezentacją obiektu klasy Product.



Przykład działania metody __str__():



[IN]: product = Product('Laptop', 3900.0)
[IN]: print(product)


[OUT]: Product Name: Laptop | Price: 3900.0


Następnie utwórz instancję klasy Product o nazwie product i przekazanych argumentach:

'Mobile Phone', 1990.0



W odpowiedzi wydrukuj instancję product do konsoli.



Oczekiwany wynik:



Product Name: Mobile Phone | Price: 1990.0"""

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

    def __str__(self):
        return f"Product Name: {self.product_name} | Price: {self.price}"


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


product = Product('Mobile Phone', 1990.0)
print(product)