"""Podana jest implementacja klasy Vector. Utwórz dwie instancje klasy Vector:

v1 = Vector(4, 2)

v2 = Vector(-1, 3)



Następnie spróbuj wykonać odejmowanie wektorów, tzn. wykonać operację v1 - v2. W przypadku błędu wydrukuj komunikat o błędzie do konsoli.



Oczekiwany wynik:



unsupported operand type(s) for -: 'Vector' and 'Vector'"""


class Vector:
    def __init__(self, *args):
        self.components = args

    def __repr__(self):
        return f"Vector{self.components}"

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


v1 = Vector(4, 2)

v2 = Vector(-1, 3)
try:
    print(v1 - v2)
except TypeError as error:
    print(error)
