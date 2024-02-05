"""Zaimplementuj klasę o nazwie Person, która ma jeden atrybut chroniony o nazwie _first_name. Kolejno zaimplementuj metodę o nazwie get_first_name(), która odczyta wartość ustawionego atrybutu chronionego _first_name. Zadeklaruj metodę o nazwie set_first_name(), która pozwoli zmodyfikować wartość atrybutu chronionego _first_name (pomiń walidację ustawianej wartości).



Następnie wykorzystując metody get_first_name(), set_first_name() oraz klasę property (zrób to w standardowy sposób) utwórz właściwość o nazwie first_name (właściwość do odczytu i modyfikacji).



Utwórz instancję klasy Person przekazując do konstruktora wartość 'John'. Następnie wykorzystując metodę set_first_name() ustaw nową wartość atrybutu na 'Mike'. W odpowiedzi wydrukuj wartość właściwości first_name do konsoli.



Oczekiwany wynik:



Mike"""

class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, new_first_name):
        self._first_name = new_first_name

    first_name = property(fget=get_first_name, fset=set_first_name)


person = Person('John')
person.set_first_name('Mike')
print(person.first_name)