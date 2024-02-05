"""Zaimplementowane są poniższe klasy:

Vehicle

LandVehicle

AirVehicle



Zdefiniuj metodę specjalną __repr__() w klasie Vehicle, która będzie zwracać formalną reprezentację obiektów klas: Vehicle, LandVehicle oraz AirVehicle.



Przykładowo poniższy kod:



instances = [Vehicle(), LandVehicle(), AirVehicle()]
 
for instance in instances:
    print(instance)


zwróci:



Vehicle(category='land vehicle')
LandVehicle(category='land vehicle')
AirVehicle(category='air vehicle')


Aby zaliczyć ćwiczenie wystarczy tylko zaimplementować metodę __repr__() i uruchom podany kod."""


class Vehicle:
    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'

    def __repr__(self):
        return f"{self.__class__.__name__}(category='{self.category}')"


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'


instances = [Vehicle(), LandVehicle(), AirVehicle()]

for instance in instances:
    print(instance)
