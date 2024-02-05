"""Zaimplementuj klasę o nazwie Person, która ma dwa atrybuty chronione o nazwach odpowiednio _first_name oraz _last_name. Kolejno zaimplementuj metody o nazwach get_first_name(), set_first_name(), get_last_name(), set_last_name(), które pozwolą odczytać i zmodyfikować odpowiednio wartość ustawionych atrybutów chronionych.



Następnie wykorzystując metody get_first_name(), set_first_name(), get_last_name(), set_last_name() oraz klasę property (zrób to w standardowy sposób) utwórz właściwości o nazwach odpowiednio first_name oraz last_name (właściwości do odczytu i modyfikacji).



Utwórz instancję klasy Person z podanymi informacjami:

first_name = 'John'

last_name = 'Dow'



Następnie wartości tych atrybutów wydrukuj do konsoli. Kolejno wykorzystując notację kropkową zmodyfikuj dla tej instancji wartości atrybutów odpowiednio:

first_name na wartość 'Tom'

last_name na wartość 'Smith'



W odpowiedzi wydrukuj atrybut __dict__ utworzonej instancji do konsoli.



Oczekiwany wynik:



John
Dow
{'_first_name': 'Tom', '_last_name': 'Smith'}"""

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, new_first_name):
        self._first_name = new_first_name

    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, new_last_name):
        self._last_name = new_last_name
    
    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)

person = Person('John', 'Dow')
print(person.first_name)
print(person.last_name)

person.first_name = 'Tom'
person.last_name = 'Smith'

print(person.__dict__)