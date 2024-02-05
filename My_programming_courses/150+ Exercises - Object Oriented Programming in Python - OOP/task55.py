"""Zaimplementuj klasę o nazwie Car, która przy tworzeniu instancji ustawi poniższe atrybuty instancji:

brand

model

price

type_of_car, domyślnie ustaw wartość 'sedan'



Następnie utwórz instancję klasy Car o nazwie car o podanych wartościach atrybutów:

brand = 'Opel'

model = 'Insignia'

price = 115000



W odpowiedzi wydrukuj wartość atrybutu __dict__ instancji car do konsoli.



Oczekiwany wynik:



{'brand': 'Opel', 'model': 'Insignia', 'price': 115000, 'type_of_car': 'sedan'}"""


class Car:
    def __init__(self, brand, model, price, type_of_car="sedan"):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car


car = Car("Opel", "Insignia", 115000)
print(car.__dict__)
