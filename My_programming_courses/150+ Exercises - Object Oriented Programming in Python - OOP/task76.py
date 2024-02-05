"""Zaimplementowana jest klasa o nazwie Pet, która ma dwie właściwości name oraz age (patrz poniżej). Dodaj walidację właściwości age na etapie tworzenia obiektu oraz modyfikacji atrybutu:

wartość atrybutu age musi być typu int, jeżeli tak nie jest zgłoś błąd TypeError o komunikacie:


'The value of age must be of type int.'


wartość atrybutu age musi być dodatnia, jeżeli tak nie jest zgłoś błąd ValueError o komunikacie:


'The value of age must be a positive integer.'


Następnie spróbuj utworzyć instancję klasy Pet o nazwie pet i wartościach atrybutów odpowiednio:

'Max'

'seven'



W przypadku błędu wydrukuj do konsoli komunikat o błędzie.



Oczekiwany wynik:



The value of age must be of type int."""


class Pet:
    def __init__(self, name, age):
        self._name = name
        if not isinstance(age, int):
            raise TypeError("The value of age must be of type int.")
        else:
            self._age = age

        if age > 0:
            self._age = age
        else:
            raise ValueError("The value of age must be a positive integer.")

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
            raise TypeError("The value of age must be of type int.")
        else:
            self._age = value

        if value > 0:
            self._age = value
        else:
            raise ValueError("The value of age must be a positive integer.")


try:
    pet = Pet('Max', 'seven')
except TypeError as error:
    print(error)
except ValueError as error:
    print(error)
