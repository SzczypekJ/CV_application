"""Zaimplementuj klasę o nazwie Vector, która przy tworzeniu instancji będzie przyjmować dowolną liczbę argumentów będących współrzędnymi wektora w przestrzeni n-wymiarowej (bez żadnej walidacji) i przypisz do atrybutu instancji o nazwie components. Następnie utwórz dwie instancje klasy Vector o poniższych współrzędnych:

(1, 2)

(4, 5, 2)



I przypisz odpowiednio do zmiennych v1 oraz v2. W odpowiedzi wydrukuj wartość atrybutu components dla obiektów v1 oraz v2 tak jak pokazano poniżej.



Oczekiwany wynik:



v1 -> (1, 2)
v2 -> (4, 5, 2)"""


class Vector:
    def __init__(self, *args):
        self.components = args


v1 = Vector(1, 2)
v2 = Vector(4, 5, 2)

print(f'v1 -> {v1.components}')
print(f'v2 -> {v2.components}')
