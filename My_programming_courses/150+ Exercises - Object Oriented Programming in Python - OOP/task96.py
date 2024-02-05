"""Zaimplementuj klasę o nazwie Vector, która przy tworzeniu instancji (metoda __init__()) będzie przyjmować dowolną liczbę argumentów będących współrzędnymi wektora w przestrzeni n-wymiarowej (bez żadnej walidacji) i przypisz do atrybutu o nazwie components.



Następnie zaimplementuj metodę specjalną __repr__() pozwalającą wyświetlić formalną reprezentację obiektu klasy Vector tak jak pokazano poniżej:



[IN]: v1 = Vector(1, 2)
[IN]: print(v1)


[Out]: Vector(1, 2)


Następnie zbuduj wektor z przestrzeni R^3 o współrzędnych: (-3, 4, 2) i przypisz do zmiennej v1. W odpowiedzi wydrukuj zmienną v1 do konsoli.



Oczekiwany wynik:



Vector(-3, 4, 2)
"""


class Vector:
    def __init__(self, *args):
        self.components = args

    def __repr__(self):
        return f"Vector{self.components}"


v1 = Vector(-3, 4, 2)
print(v1)
