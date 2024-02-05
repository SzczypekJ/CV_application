"""Podana jest implementacja klasy Vector. Zaimplementuj metodę specjalną __bool__() pozwalającą zwrócić wartość logiczną wektora:

False w przypadku, gdy pierwsza współrzędna jest zerem

True przeciwnie



W przypadku, gdy użytkownik nie przekaże żadnego argumentu zwróć wartość logiczną False.



Przykład:



[IN]: v1 = Vector(0, 4, 5)
[IN]: print(bool(v1))


[Out]: False


Następnie zbuduj podane instancje klasy Vector:

v1 = Vector()

v2 = Vector(3, 2)

v3 = Vector(0, -3, 2)

v4 = Vector(5, 0, -1)



W odpowiedzi wydrukuj wartości logiczne podanych instancji w odpowiedniej kolejności.



Oczekiwany wynik:



False
True
False
True"""


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __bool__(self):
        if not self.components:
            return False
        return False if self.components[0] == 0 else True


v1 = Vector()

v2 = Vector(3, 2)

v3 = Vector(0, -3, 2)

v4 = Vector(5, 0, -1)
print(bool(v1))
print(bool(v2))
print(bool(v3))
print(bool(v4))
