"""Zaimplementowano klasę o nazwie Car, która przy tworzeniu instancji ustawia poniższe atrybuty instancji:

brand

model

price

type_of_car, domyślnie wartość 'sedan'



Następnie utwórz instancję klasy Car o nazwie car o podanych wartościach atrybutów:

brand = 'BMW'

model = 'X3'

price = 200000

type_of_car = 'SUV'



W odpowiedzi wydrukuj wartość atrybutu __dict__ instancji car do konsoli.



Oczekiwany wynik:



{'brand': 'BMW', 'model': 'X3', 'price': 200000, 'type_of_car': 'SUV'}"""


class Car:
    def __init__(self, brand, model, price, type_of_car=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car if type_of_car else 'sedan'


car = Car("BMW", "X3", 200000, "SUV")
print(car.__dict__)
