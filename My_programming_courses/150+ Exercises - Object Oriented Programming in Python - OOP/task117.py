"""Zaimplementowane są poniższe klasy:

Vehicle

LandVehicle

AirVehicle



Zdefiniuj metodę display_info() w klasie Vehicle pozwalającą wyświetlać nazwę klasy wraz z wartością atrybutu category. Metoda ma działać z poziomu wszystkich klas.



Przykładowo poniższy kod:



instances = [Vehicle(), LandVehicle(), AirVehicle()]
 
for instance in instances:
    print(instance)


zwróci:



Vehicle -> land vehicle
LandVehicle -> land vehicle
AirVehicle -> air vehicle


Aby zaliczyć ćwiczenie wystarczy tylko zaimplementować metodę display_info() i uruchomić podany kod."""


class Vehicle:
    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'

    def display_info(self):
        print(f"{self.__class__.__name__} -> {self.category}")


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'


vehicles = [Vehicle(), LandVehicle(), AirVehicle()]

for vehicle in vehicles:
    vehicle.display_info()
