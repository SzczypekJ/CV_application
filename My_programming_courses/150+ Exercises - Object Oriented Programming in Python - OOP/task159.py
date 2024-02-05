"""Podana jest implementacja klas: Product oraz Warehouse. Dokończ implementację metody o nazwie search_product() klasy Warehouse pozwalającą zwrócić listę produktów (atrybut products instancji klasy Warehouse) zawierających podaną nazwę (argument query).



Następnie utwórz instancję klasy Warehouse o nazwie warehouse i wykonaj poniższy kod:



warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)


W odpowiedzi wywołaj metodę search_product() i znajdź wszystkie produkty zawierające literę 'M'.



Oczekiwany wynik:



[Product(product_name='Mobile Phone', price=1990.0), Product(product_name='Mouse', price=49.0)]"""

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

    def display_products(self):
        for product in self.products:
            print(f'Product ID: {product.product_id} | Product name: '
                  f'{product.product_name} | Price: {product.price}')

    def sort_by_price(self, ascending=True):
        return sorted(self.products, key=lambda product: product.price,
                      reverse=not ascending)

    def split(self, word):
        return list(word)

    def search_product(self, query):
        lst = []
        for product in self.products:
            if query in self.split(product.product_name):
                lst.append(product)
        print(lst)


warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
warehouse.search_product("M")
