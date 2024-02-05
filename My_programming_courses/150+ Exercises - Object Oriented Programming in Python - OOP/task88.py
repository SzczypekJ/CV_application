"""Zaimplementuj klasę o nazwie Person, która będzie posiadać atrybut klasy o nazwie instances będący pustą listą. Następnie przy każdym utworzeniu instancji klasy Person dodawaj ją do listy Person.instances (wykorzystaj do tego metodę __init__()).



Zaimplementuj także metodę klasy o nazwie count_instances() pozwalającą zwrócić liczbę utworzonych obiektów klasy Person.



Utwórz w dowolny sposób trzy instancje klasy Person, następnie wydrukuj do konsoli wywołanie metody count_instances().



Oczekiwany wynik:



3"""


class Person:
    instances = []

    def __init__(self):
        Person.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(Person.instances)


person1 = Person()
person2 = Person()
person3 = Person()
print(Person.count_instances())
