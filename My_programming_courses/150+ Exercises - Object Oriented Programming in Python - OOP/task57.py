"""Zaimplementuj klasę o nazwie Laptop, która przy tworzeniu instancji ustawi poniższe atrybuty instancji:

brand

model

price



Przy tworzeniu instancji dodaj walidację dla atrybutu price. Wartość atrybutu price musi być obiektem typu int lub float większym od zera. Jeżeli tak nie jest podnieś błąd TypeError o treści:



'The price attribute must be a positive int or float.'


Następnie utwórz instancję o nazwie laptop klasy Laptop o podanych wartościach atrybutów:

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
        if not isinstance(price, (int, float)):
            if not price > 0:
                raise TypeError(
                    "The price attribute must be a positive int or float.")
        else:
            self.price = price


laptop = Laptop("Acer", "Predator", 5490)
print(laptop.__dict__)
