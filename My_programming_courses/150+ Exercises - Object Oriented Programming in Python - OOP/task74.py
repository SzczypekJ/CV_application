"""Zaimplementuj klasę o nazwie Pet, która ma jeden atrybut chroniony instancji o nazwie _name. Następnie wykorzystując dekorator @property utwórz właściwość o nazwie name (właściwość do odczytu i do modyfikacji, nie dodawaj żadnej walidacji ustawianej wartości).



Utwórz instancję klasy Pet o nazwie pet i ustaw atrybut name na wartość 'Max'. Następnie wykorzystując notację kropkową zmodyfikuj wartość atrybutu name na 'Oscar'. W odpowiedzi wydrukuj zawartość atrybutu __dict__ instancji pet do konsoli.



Oczekiwany wynik:



{'_name': 'Oscar'}"""


class Pet:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


pet = Pet(name="Max")
pet.name = "Oscar"
print(pet.__dict__)
