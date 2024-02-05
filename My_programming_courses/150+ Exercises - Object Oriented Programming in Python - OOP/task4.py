"""Poniżej podana jest klasa Product oraz instancja tej klasy o nazwie product. Wyświetl przestrzeń nazw (wartość atrybutu __dict__) tej instancji do konsoli tak jak pokazano poniżej.



Oczekiwany wynik:



{'product_name': 'Mobile Phone', 'product_id': '54274', 'price': 2900}
"""

import uuid


class Product:
    def __init__(self, product_name, product_id, price):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return (
            f"Product(product_name='{self.product_name}', "
            f"price={self.price})"
        )


product = Product('Mobile Phone', '54274', 2900)

print(product.__dict__)
