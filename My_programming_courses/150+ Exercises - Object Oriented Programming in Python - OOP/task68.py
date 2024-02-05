"""Zaimplementuj klasę o nazwie Person, która ma dwa atrybuty chronione instancji o nazwach odpowiednio _first_name oraz _last_name. Kolejno zaimplementuj metody o nazwach get_first_name() oraz get_last_name(), które odczytają odpowiednio wartość ustawionych atrybutów chronionych _first_name oraz _last_name. Następnie wykorzystując metody get_first_name() oraz get_last_name() oraz klasę property (zrób to w standardowy sposób) utwórz dwie właściwości o nazwach odpowiednio first_name oraz last_name (właściwości tylko do odczytu).



Następnie utwórz instancję klasy Person i ustaw:

first_name na wartość 'John'

last_name na wartość 'Dow'



Wydrukuj wartości atrybutów first_name oraz last_name utworzonej instancji do konsoli.



Oczekiwany wynik:



John
Dow"""


class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    first_name = property(fget=get_first_name)
    last_name = property(fget=get_last_name)


person = Person('John', 'Dow')

print(person.first_name)
print(person.last_name)
