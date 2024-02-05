"""Zaimplementowane są klasy o następującej strukturze:

Container

TemperatureControlledContainer

RefrigeratedContainer



Klasa TemperatureControlledContainer dziedziczy po klasie Container, zaś klasa RefrigeratedContainer dziedziczy po klasie TemperatureControlledContainer. Do klasy TemperatureControlledContainer dodaj atrybut klasy o nazwie temp_range przechowujący tuplę (-25.0, 25.0), zaś do klasy RefrigeratedContainer atrybut klasy o tej samej nazwie i wartości (-25.0, 5.0).



Następnie wykorzystując funkcję getattr() odczytaj wartość atrybutu temp_range klasy RefrigeratedContainer i wydrukuj do konsoli.



Oczekiwany wynik:



(-25.0, 5.0)"""


class Container:
    category = 'general purpose'


class TemperatureControlledContainer(Container):
    temp_range = (-25.0, 25.0)


class RefrigeratedContainer(TemperatureControlledContainer):
    temp_range = (-25.0, 5.0)


print(getattr(RefrigeratedContainer, 'temp_range'))
