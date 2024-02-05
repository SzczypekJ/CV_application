"""Zaimplementowana jest klasa o nazwie Person. Zmodyfikuj metodę __init__() tak, aby można było ustawić dwa atrybuty instancji o nazwie first_name oraz last_name (publiczne atrybuty, bez żadnej walidacji). Zwróć uwagę na moment dodania instancji do listy instances (dodanie instancji powinno nastąpić po przypisaniu atrybutów).



Następnie utwórz dwie instancje klasy Person o dowolnych wartościach atrybutów. W odpowiedzi wydrukuj wywołanie metody count_instances() na dowolnej z tych instancji.



Oczekiwany wynik:



2"""


class Person:
    instances = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(Person.instances)


person1 = Person("Jakub", "Szczypek")
person2 = Person("John", "Smith")
print(person1.count_instances())
