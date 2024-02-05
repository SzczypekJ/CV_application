"""Podana jest klasa Note (reprezentacja notatki). Zaimplementuj klasę Notebook (reprezentacja notatnika z notatkami) z dwoma metodami:

__init__() tworzącą atrybut instancji klasy Notebook o nazwie notes będący pustą listą, w której będą przechowywane notatki.

new_note() tworząca nowy obiekt klasy Note i dodająca go do listy notes



Utwórz instancję klasy Notebook o nazwie notebook. Następnie wykorzystując metodę new_note() dodaj dwie notatki do notatnika o następującej treści:

'My first note.'

'My second note.'



W odpowiedzi wydrukuj zawartość atrybutu notes instancji notebook do konsoli.



Oczekiwany wynik:



[Note(content='My first note.'), Note(content='My second note.')]"""

import datetime


class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S'
        )

    def __repr__(self):
        return f"Note(content='{self.content}')"

    def find(self, word):
        return word.lower() in self.content.lower()


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, content):
        new_note = Note(content)
        self.notes.append(new_note)


notebook = Notebook()
notebook.new_note('My first note.')
notebook.new_note('My second note.')
print(notebook.notes)
