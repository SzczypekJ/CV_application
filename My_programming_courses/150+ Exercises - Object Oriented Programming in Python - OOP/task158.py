"""Podana jest implementacja klas: Product oraz Warehouse. Do klasy Warehouse dodaj metodę o nazwie sort_by_price() pozwalającą zwrócić posortowaną alfabetycznie listę produktów (atrybut products instancji klasy Warehouse). Metoda sort_by_price() przyjmuje także argument ascending domyślnie ustawiony na wartość True, co oznacza sortowanie rosnąco. W przypadku przekazania wartości False odwróć porządek sortowania.



Następnie utwórz instancję klasy Warehouse o nazwie warehouse i wykonaj poniższy kod:



warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)


W odpowiedzi wykorzystując metodę sort_by_price() wydrukuj do konsoli posortowaną listę produktów tak jak pokazano poniżej.



Oczekiwany wynik:



Product(product_name='USB Cable', price=24.9)
Product(product_name='Mouse', price=49.0)
Product(product_name='Mobile Phone', price=1990.0)
Product(product_name='Camera', price=2900.0)
Product(product_name='Laptop', price=3900.0)"""


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
        return self.products.sort(key=lambda x: x.price, reverse=not ascending)
        #         return sorted(
        #     self.products,
        #     key=lambda product: product.price,
        #     reverse=not ascending,
        # )


warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
warehouse.sort_by_price()
for i in warehouse.products:
    print(i)
