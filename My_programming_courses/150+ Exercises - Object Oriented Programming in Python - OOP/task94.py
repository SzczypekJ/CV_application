"""Zdefiniuj klasę Person przyjmującą dwa publiczne atrybuty fname (first name) oraz lname (last name). Następnie zaimplementuj metodę specjalną __repr__() pozwalającą wyświetlić formalną reprezentację obiektu klasy Person tak jak pokazano poniżej:



[IN]: person = Person('John', 'Doe')
[IN]: print(person)


[OUT]: Person(fname='John', lname='Doe')


Utwórz instancję klasy Person z podanymi atrybutami i przypisz do zmiennej person:

fname = 'Mike'

lname = 'Smith'



W odpowiedzi wydrukuj instancję person do konsoli.



Oczekiwany wynik:



Person(fname='Mike', lname='Smith')"""


class Person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def __repr__(self) -> str:
        return f"Person(fname='{self.fname}', lname='{self.lname}')"


person = Person("Mike", "Smith")
print(person)
