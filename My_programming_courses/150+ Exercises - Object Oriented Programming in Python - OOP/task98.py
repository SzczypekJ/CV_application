"""Podana jest implementacja klasy Vector. Zaimplementuj metodę specjalną __len__() pozwalającą zwrócić liczbę współrzędnych wektora.



Przykład:



[IN]: v1 = Vector(3, 4, 5)
[IN]: print(len(v1))


[Out]: 3


Następnie zbuduj wektor z przestrzeni R^3 o współrzędnych: (-3, 4, 2) i przypisz do zmiennej v1. W odpowiedzi wydrukuj liczbę współrzędnych tego wektora używając funkcji wbudowanej len().



Oczekiwany wynik:



3"""


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)


v1 = Vector(-3, 4, 2)
print(len(v1))
