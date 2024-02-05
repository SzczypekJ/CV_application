"""Podana jest klasa Person oraz lista people. Posortuj obiekty w liście people po atrybucie age rosnąco. Następnie wydrukuj do konsoli imię oraz wiek każdej osoby tak jak pokazano poniżej.



Oczekiwany wynik:



Alice -> 19
Tom -> 25
Mike -> 27
John -> 29"""


from numpy import append


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [
    Person('Tom', 25),
    Person('John', 29),
    Person('Mike', 27),
    Person('Alice', 19),
]
people.sort(key=lambda person: person.age)

for person in people:
    print(f'{person.name} -> {person.age}')
