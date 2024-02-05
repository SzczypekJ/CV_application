"""Zdefiniowane są poniższe klasy. Do klasy Person dodaj metodę __init__(), która ustawi trzy atrybuty:

first_name

last_name

age



Następnie utwórz instancję klasy Worker przekazując następujące argumenty:

'John'

'Doe'

30



W odpowiedzi wydrukuj wartość atrybutu __dict__ utworzonej instancji do konsoli.



Oczekiwany wynik:



{'first_name': 'John', 'last_name': 'Doe', 'age': 30}"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:
    pass


class Worker(Person, Department):
    pass


worker = Worker("John", "Doe", 30)
print(worker.__dict__)
