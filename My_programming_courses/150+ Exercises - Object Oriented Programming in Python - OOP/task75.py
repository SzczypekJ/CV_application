"""Zaimplementuj klasę o nazwie Pet, która ma dwa atrybuty chronione instancji o nazwach odpowiednio _name oraz _age. Następnie wykorzystując dekorator @property utwórz właściwości o nazwach odpowiednio name oraz age (właściwości do odczytu i do modyfikacji, nie dodawaj żadnej walidacji ustawianej wartości).



Utwórz instancję klasy Pet o nazwie pet i atrybutach kolejno:

name = 'Max'

age = 5



Wydrukuj atrybut __dict__ instancji pet do konsoli. Następnie dokonaj modyfikacji atrybutów wykorzystują notację kropkową:

name na wartość 'Tom'

age na wartość 8



I jeszcze raz wydrukuj atrybut __dict__ instancji pet do konsoli.



Oczekiwany wynik:



{'_name': 'Max', '_age': 5}
{'_name': 'Tom', '_age': 8}"""


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

    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value


pet = Pet("Max", 5)
print(pet.__dict__)
pet.name = "Tom"
pet.age = 8
print(pet.__dict__)
