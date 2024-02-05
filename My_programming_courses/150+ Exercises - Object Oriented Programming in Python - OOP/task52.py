"""Zaimplementowano klasę o nazwie Laptop, która przy tworzeniu instancji ustawia poniższe atrybuty instancji:

brand

model

price



Zaimplementuj w klasie Laptop metodę o nazwie display_attrs_with_values(), która wyświetli nazwy wszystkich atrybutów instancji klasy Laptop wraz z ich wartościami tak jak pokazano poniżej (nazwa atrybutu -> wartość atrybutu).



Następnie utwórz instancję klasy Laptop o nazwie laptop o podanych wartościach atrybutów:

brand = 'Dell'

model = 'Inspiron'

price = 3699



W odpowiedzi wywołaj metodę display_attrs_with_values() na instancji laptop.



Oczekiwany wynik:



brand -> Dell
model -> Inspiron
price -> 3699"""


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_attrs_with_values(self):
        for attr, value in self.__dict__.items():
            print(f"{attr} -> {value}")


laptop = Laptop('Dell', 'Inspiron', 3699)
laptop.display_attrs_with_values()