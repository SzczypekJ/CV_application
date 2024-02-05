"""Zaimplementuj klasę o nazwie Pet, która ma jeden atrybut chroniony instancji o nazwie _name. Kolejno zaimplementuj metodę o nazwie name(), która odczyta wartość ustawionego atrybutu chronionego _name. Następnie wykorzystując dekorator @property utwórz właściwość o nazwie name (właściwość tylko do odczytu).



Utwórz instancję klasy Pet o nazwie pet i ustaw atrybut name na wartość 'Max'. W odpowiedzi wydrukuj zawartość atrybutu __dict__ instancji pet do konsoli.



Oczekiwany wynik:



{'_name': 'Max'}"""

class Pet:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

pet = Pet('Max')
print(pet.__dict__)