"""Zaimplementuj klasę o nazwie Person, która ma jeden atrybut chroniony instancji o nazwie _first_name. Kolejno zaimplementuj metodę o nazwie get_first_name(), która odczyta wartość ustawionego atrybutu chronionego _first_name. Następnie wykorzystując metodę get_first_name() oraz klasę property (zrób to w standardowy sposób) utwórz właściwość o nazwie first_name (właściwość tylko do odczytu).



Kolejno utwórz instancję klasy Person przekazując do konstruktora wartość 'John'. Wydrukuj wartość właściwości first_name utworzonej instancji do konsoli.



Oczekiwany wynik:



John"""


class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    first_name = property(
        fget=get_first_name
    )


person = Person("John")
print(person.first_name)
