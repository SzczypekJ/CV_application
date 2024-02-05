"""Zdefiniowane są poniższe klasy. Do klasy Worker dodaj metodę __init__() ustawiającą wszystkie atrybuty z klas Person oraz Department. Następnie utwórz instancję klasy Worker przekazując kolejno argumenty:

'John'

'Doe'

30

'Information Technology'

'IT'



W odpowiedzi wydrukuj wartość atrybutu __dict__ utworzonej instancji do konsoli.



Oczekiwany wynik:



{'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'dept_name': 'Information Technology', 'short_dept_name': 'IT'}
"""

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:
    def __init__(self, dept_name, short_dept_name):
        self.dept_name = dept_name
        self.short_dept_name = short_dept_name


class Worker(Person, Department):
    def __init__(self, first_name, last_name, age, dept_name, short_dept_name):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name, short_dept_name)

worker = Worker('John', 'Doe', 30, 'Information Technology', 'IT')
print(worker.__dict__)