"""Zaimplementowana jest klasa o nazwie Pet, która ma dwie właściwości name oraz age (patrz poniżej). Utwórz instancję klasy Pet o nazwie pet i wartościach atrybutów odpowiednio:

'Max'

7



Następnie spróbuj zmodyfikować wartość atrybutu age instancji pet na -10. W przypadku błędu wydrukuj do konsoli komunikat o błędzie do konsoli.



Oczekiwany wynik:



The value of age must be a positive integer."""

class Pet:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('The value of age must be of type int.')
        if not value > 0:
            raise ValueError('The value of age must be a positive integer.')
        self._age = value

try:
    pet = Pet("Max", 7)
except TypeError as error:
    print(error)
except ValueError as error:
    print(error)

try:
    pet.age = -10
except TypeError as error:
    print(error)
except ValueError as error:
    print(error)
