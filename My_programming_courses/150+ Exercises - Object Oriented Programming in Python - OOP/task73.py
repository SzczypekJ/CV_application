"""Zaimplementuj klasę o nazwie Pet, która ma dwa atrybuty chronione instancji o nazwach odpowiednio _name oraz _age. Kolejno zaimplementuj metody o nazwach name() oraz age(), które odczytają odpowiednio wartość ustawionych atrybutów chronionych.



Następnie wykorzystując dekorator @property utwórz właściwości o nazwach odpowiednio name oraz age (właściwości tylko do odczytu).



Utwórz instancję klasy Pet o nazwie pet i ustaw atrybut name na wartość 'Max' oraz age na wartość 5. W odpowiedzi wydrukuj zawartość atrybutu __dict__ instancji pet do konsoli.



Oczekiwany wynik:



{'_name': 'Max', '_age': 5}"""


class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


pet = Pet("Max", 5)
print(pet.__dict__)
