"""Zaimplementowana jest klasa Person. Dodaj metodę specjalną __str__() pozwalającą zwracać nieformalną reprezentację instancji klasy Person.



Przykład:



[IN]: person = Person('Mike', 'Smith')
[IN]: print(person)


First name: Mike
Last name: Smith


Następnie utwórz instancję o nazwie person z wartościami atrybutów:

fname = 'John'

lname = 'Doe'



W odpowiedzi wydrukuj instancję person do konsoli.



Oczekiwany wynik:



First name: John
Last name: Doe"""


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"

    def __str__(self):
        return f"First name: {self.fname}\nLast name: {self.lname}"


person = Person("John", "Doe")
print(person)
