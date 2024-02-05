"""Podana jest implementacja klasy Vector. Zaimplementuj metodę specjalną __str__() pozwalającą wyświetlić nieformalną reprezentację obiektu klasy Vector tak jak pokazano poniżej:



[IN]: v1 = Vector(1, 2)
[IN]: print(v1)


[Out]: (1, 2)


Następnie zbuduj wektor z przestrzeni R^3 o współrzędnych: (-3, 4, 2) i przypisz do zmiennej v1. W odpowiedzi wydrukuj zmienną v1 do konsoli.



Oczekiwany wynik:



(-3, 4, 2)"""


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components[:]}'


v1 = Vector(-3, 4, 2)
print(v1)
