"""Zaimplementuj klasę o nazwie Laptop, która przy tworzeniu instancji ustawi poniższe atrybuty instancji:

brand

model

price



Następnie utwórz instancję klasy Laptop o nazwie laptop o podanych wartościach atrybutów:

brand = 'Acer'

model = 'Predator'

price = 5490



W odpowiedzi wydrukuj wartość atrybutu __dict__ instancji laptop do konsoli.



Oczekiwany wynik:



{'brand': 'Acer', 'model': 'Predator', 'price': 5490}"""


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


laptop = Laptop('Acer', 'Predator', 5490)
print(laptop.__dict__)
