"""Zaimplementowano klasę o nazwie Person, która posiada atrybut chroniony o nazwie _first_name. Kolejno zaimplementowano metody o nazwach get_first_name(), set_first_name(), które pozwolą odczytać i zmodyfikować wartość ustawionego atrybutu chronionego _first_name.



Zaimplementuj metodę del_first_name() pozwalającą usuwać atrybut chroniony _first_name. Następnie wykorzystując metody get_first_name(), set_first_name(), del_first_name() oraz klasę property (zrób to w standardowy sposób) utwórz właściwość o nazwie first_name (właściwości do odczytu, modyfikacji i usuwania).



Utwórz instancję klasy Person o nazwie person przekazując do konstruktora wartość 'Tom'. Wykorzystując metodę del_first_name() usuń atrybut first_name instancji person. W odpowiedzi wyświetl atrybut __dict__ instancji person do konsoli.



Oczekiwany wynik:



{}"""


class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        self._first_name = value

    def del_first_name(self):
        del self._first_name

    first_name = property(fget=get_first_name,
                          fset=set_first_name,
                          fdel=del_first_name
                          )


person = Person("Tom")
person.del_first_name()
print(person.__dict__)
