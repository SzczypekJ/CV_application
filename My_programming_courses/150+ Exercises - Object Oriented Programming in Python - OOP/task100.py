"""Podana jest implementacja klasy Vector. Utwórz dwie instancje klasy Vector:

v1 = Vector(4, 2)

v2 = Vector(-1, 3)



Następnie spróbuj wykonać dodawanie tych instancji, tzn. wykonać operację v1 + v2. W przypadku błędu wydrukuj komunikat o błędzie do konsoli.



Oczekiwany wynik:



unsupported operand type(s) for +: 'Vector' and 'Vector'"""

from os import error


class Vector:
    def __init__(self, *args):
        self.components = args

    def __repr__(self):
        return f"Vector{self.components}"

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)


v1 = Vector(4, 2)

v2 = Vector(-1, 3)

try:
    v1 + v2
# solution 1
except TypeError:
    print("unsupported operand type(s) for +: 'Vector' and 'Vector'")
# solution 2
# except TypeError as error:
#     print(error)