"""Zaimplementowane są puste klasy o następującej strukturze:

Container

TemperatureControlledContainer

RefrigeratedContainer



Wykorzystując funkcję wbudowaną issubclass() sprawdź, czy:

klasa TemperatureControlledContainer jest klasą pochodną klasy Container

klasa RefrigeratedContainer jest klasą pochodną klasy TemperatureControlledContainer

klasa RefrigeratedContainer jest klasą pochodną klasy Container



W odpowiedzi otrzymane wartości logiczne wydrukuj do konsoli.



Oczekiwany wynik:



True
True
True"""

class Container:
    pass


class TemperatureControlledContainer(Container):
    pass


class RefrigeratedContainer(TemperatureControlledContainer):
    pass

print(issubclass(TemperatureControlledContainer, Container))
print(issubclass(RefrigeratedContainer , TemperatureControlledContainer))
print(issubclass(RefrigeratedContainer  , Container))