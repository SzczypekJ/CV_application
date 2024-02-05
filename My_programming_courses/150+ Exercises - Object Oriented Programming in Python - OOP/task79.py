"""Zaimplementuj klasę o nazwie Game, która ma właściwość o nazwie level (właściwość do odczytu i modyfikacji, domyślnie przyjmuje wartość 0). Wartość atrybutu level powinna być liczbą całkowitą z przedziału [0, 100]. Dodaj walidację na poziomie tworzenia instancji oraz modyfikacji atrybutu. Jeżeli ustawiana wartość nie jest typu int zgłoś błąd TypeError o treści:



'The value of level must be of type int.'


Jeżeli ustawiana wartość wykracza poza granice przedziału [0, 100], ustaw przekroczoną wartość brzegową (odpowiednio 0 lub 100). Następnie utwórz listę o nazwie games składającą się z czterech instancji klasy Game:



games = [Game(), Game(10), Game(-10), Game(120)]


Iterując po liście games wydrukuj wartości atrybutu level każdej z tych instancji.



Oczekiwany wynik:



0
10
0
100"""


class Game:
    def __init__(self, level=0):
        if level < 0:
            self.level = 0
        elif level > 100:
            self.level = 100
        else:
            self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise TypeError('The value of level must be of type int.')
        if value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value


try:
    games = [Game(), Game(10), Game(-10), Game(120)]
except TypeError as error:
    print(error)

for game in games:
    print(game.level)
