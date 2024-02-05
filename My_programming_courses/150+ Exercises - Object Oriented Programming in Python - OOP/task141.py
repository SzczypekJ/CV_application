"""Podana jest klasa Note. Zaimplementuj metodę find(), która pozwoli sprawdzić czy podane słowo znajduje się w notatce (wielkość liter ma znaczenie). Metoda będzie zwracać odpowiednio True lub False.



Następnie utwórz instancję o nazwie note1 z treścią notatki:



'Object Oriented Programming in Python.'


Na utworzonej instancji wykorzystując metodę find() sprawdź, czy notatka zawiera słowa:

'python'

'Python'



Wyniki wywołań metody wydrukuj do konsoli.



Oczekiwany wynik:



False
True"""

import datetime


class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S'
        )

    def find(self, word):
        return word in self.content


note1 = Note('Object Oriented Programming in Python.')
print(note1.find('python'))
print(note1.find('Python'))
