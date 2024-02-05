"""Zaimplementowane są poniższe klasy:

Container

PlasticContainer

MetalContainer

CustomContainer



Wykorzystując funkcję wbudowaną issubclass(), sprawdź czy klasy są podklasami klasy Container (inaczej są klasami pochodnymi klasy Container).

PlasticContainer

MetalContainer

CustomContainer



Wynik wydrukuj do konsoli tak jak pokazano poniżej:



True
True
False"""


class Container:
    pass


class PlasticContainer(Container):
    pass


class MetalContainer(Container):
    pass


class CustomContainer:
    pass


print(issubclass(PlasticContainer, Container))
print(issubclass(MetalContainer, Container))
print(issubclass(CustomContainer, Container))
