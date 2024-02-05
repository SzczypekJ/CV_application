"""Zaimplementowano klasę o nazwie Laptop, która przy tworzeniu instancji ustawia poniższe atrybuty instancji:

brand

model

price



Zaimplementuj w klasie Laptop metodę o nazwie display_instance_attrs(), która wyświetli nazwy wszystkich atrybutów instancji klasy Laptop.



Następnie utwórz instancję klasy Laptop o nazwie laptop o podanych wartościach atrybutów:

brand = 'Dell'

model = 'Inspiron'

price = 3699



W odpowiedzi wywołaj metodę display_instance_attrs() na instancji laptop do konsoli.



Oczekiwany wynik:



brand
model
price"""


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_instance_attrs(self):
        # solution 1 - bad solution
        # print("brand")
        # print("model")
        # print("price")

        # solution 2 - better because its works every time
        for attr in self.__dict__:
            print(attr)


laptop = Laptop("Dell", "Inspiron", 3699)
laptop.display_instance_attrs()
