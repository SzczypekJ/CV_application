"""Podane są poniższe klasy Vehicle oraz Car. Rozszerz działanie metody display_attrs() w klasie pochodnej Car, tak aby przed wyświetleniem atrybutów została wyświetlona informacja: Calling from class: Car a następnie reszta atrybutów wraz z ich wartościami. Wykorzystaj w tym celu wywołanie super(). Przykładowo dla klasy Car:



car = Car('Tesla', 'red', 2020, 190)
car.display_attrs()


Calling from class: Car
brand -> Tesla
color -> red
year -> 2020
horsepower -> 190


Następnie utwórz instancję klasy Car o nazwie car z wartościami atrybutów odpowiednio: 'Tesla', 'black', 2018, 260  W odpowiedzi wywołaj metodę display_attrs() na instancji car.



Oczekiwany wynik:



Calling from class: Car
brand -> Tesla
color -> black
year -> 2018
horsepower -> 260"""


class Vehicle:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def display_attrs(self):
        for attr, value in self.__dict__.items():
            print(f'{attr} -> {value}')


class Car(Vehicle):
    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower

    def display_attrs(self):
        print(f"Calling from class: {self.__class__.__name__}")
        super().display_attrs()


car = Car('Tesla', 'black', 2018, 260)
car.display_attrs()
