"""Zdefiniowane są poniższe klasy. Do klasy Department dodaj metodę __init__(), która ustawi atrybut:

dept_name (nazwa departamentu)

short_dept_name (skrócona nazwa departamentu)



Następnie utwórz instancję klasy Department przekazując argumenty:

'Information Technology'

'IT'



W odpowiedzi wydrukuj wartość atrybutu __dict__ utworzonej instancji do konsoli.



Oczekiwany wynik:



{'dept_name': 'Information Technology', 'short_dept_name': 'IT'}"""


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
    pass


department = Department('Information Technology', 'IT')
print(department.__dict__)
