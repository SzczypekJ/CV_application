"""Podana jest klasa Vehicle, która posiada trzy atrybuty:

brand

color

year



Utwórz klasę Car, która dziedziczy po klasie Vehicle. Następnie nadpisz metodę __init__() tak, aby klasa Car w konstruktorze przyjmowała cztery poniższe argumenty i ustawiała je odpowiednio jako atrybuty instancji:

brand

color

year

horsepower



Nie wykorzystuj w tym przypadku wywołania super(). Następnie utwórz po jednej instancji klas odpowiednio:

o nazwie vehicle i wartościach atrybutów kolejno: 'Tesla', 'red', 2020

o nazwie car i wartościach atrybutów kolejno: 'Tesla', 'red', 2020, 300



W odpowiedzi wydrukuj wartości atrybutu __dict__ instancji vehicle oraz car do konsoli.



Oczekiwany wynik:



{'brand': 'Tesla', 'color': 'red', 'year': 2020}
{'brand': 'Tesla', 'color': 'red', 'year': 2020, 'horsepower': 300}"""


class Vehicle:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


class Car(Vehicle):
    def __init__(self, brand, color, year, horsepower):
        self.brand = brand
        self.color = color
        self.year = year
        self.horsepower = horsepower

vehicle = Vehicle("Tesla", "red", 2020)
car = Car("Tesla", "red", 2020, 300)
print(vehicle.__dict__)
print(car.__dict__)