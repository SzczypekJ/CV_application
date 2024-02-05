"""Zaimplementuj puste klasy o następującej strukturze:

Container

TemperatureControlledContainer

RefrigeratedContainer



Klasa TemperatureControlledContainer dziedziczy po klasie Container, zaś klasa RefrigeratedContainer dziedziczy po klasie TemperatureControlledContainer."""


class Container:
    pass


class TemperatureControlledContainer(Container):
    pass


class RefrigeratedContainer(TemperatureControlledContainer):
    pass
