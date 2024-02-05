"""Podane są poniższe klasy Vehicle oraz Car. Zaimplementuj metodę o nazwie display_attrs() w klasie bazowej Vehicle, która pozwoli wyświetlić atrybuty instancji wraz z ich wartościami.



Przykładowo dla klasy Vehicle:



vehicle = Vehicle('Tesla', 'red', 2020)
vehicle.display_attrs()


brand -> Tesla
color -> red
year -> 2020


Oraz dla klasy Car:



car = Car('Tesla', 'red', 2020, 190)
car.display_attrs()


brand -> Tesla
color -> red
year -> 2020
horsepower -> 190


Następnie utwórz instancję klasy Car o nazwie car z wartościami atrybutów odpowiednio: 'Opel', 'black', 2018, 160  W odpowiedzi wywołaj metodę display_attrs() na instancji car.



Oczekiwany wynik:



brand -> Opel
color -> black
year -> 2018
horsepower -> 160"""

class Vehicle:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def display_attrs(self):
        for attr, value in self.__dict__.items():
            print(f"{attr} -> {value}")

class Car(Vehicle):
    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower

car = Car('Opel', 'black', 2018, 160)
car.display_attrs()