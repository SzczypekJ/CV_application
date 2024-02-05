"""Zaimplementuj klasę o nazwie Note, która będzie opisywać prostą notatkę. Przy tworzeniu obiektów klasy Note zostanie ustawiony atrybut instancji o nazwie content z zawartością notatki. Wykorzystując moduł datetime dodaj także czas utworzenia notatki jako atrybut instancji o nazwie creation_time.



Następnie utwórz dwie instancje klasy Note o nazwie note1 oraz note2 i przypisz następujące treści notatek:

'My first note.'

'My second note.'



Uwaga! Atrybut creation_time będzie miał zmienną wartość. Zachowaj podany format daty: '%m-%d-%Y %H:%M:%S'"""

from datetime import datetime


class Note:
    def __init__(self, content):
        self.content = content
        self.now = datetime.now()
        self.creation_time = self.now.strftime('%m-%d-%Y %H:%M:%S')


note1 = Note("My first note.")
note2 = Note("My second note.")
