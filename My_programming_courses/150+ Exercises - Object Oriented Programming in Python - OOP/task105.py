"""Podana jest implementacja klasy Vector. Zaimplementuj metodę specjalną __truediv__(), która pozwoli dzielić instancje klasy Vector po współrzędnych. Dla prostoty załóż, że użytkownik dzieli wektory o tej samej długości oraz współrzędne drugiego wektora są różne od zera. Następnie utwórz dwie instancje klasy Vector:

v1 = Vector(4, 2)

v2 = Vector(-1, 4)



Kolejno wykonaj operację dzielenia tych wektorów. W odpowiedzi wydrukuj wektor wynikowy do konsoli.



Oczekiwany wynik:



(-4.0, 0.5)"""


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        components = tuple(
            x + y
            for x, y in zip(self.components, other.components)
        )
        return Vector(*components)

    def __sub__(self, other):
        components = tuple(
            x - y
            for x, y in zip(self.components, other.components)
        )
        return Vector(*components)

    def __mul__(self, other):
        components = tuple(
            x * y
            for x, y in zip(self.components, other.components)
        )
        return Vector(*components)

    def __truediv__(self, other):
        components = tuple(
            x / y
            for x, y in zip(self.components, other.components)
        )
        return Vector(*components)


v1 = Vector(4, 2)

v2 = Vector(-1, 4)
print(v1 / v2)
