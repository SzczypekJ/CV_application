"""Podane są implementacje klasy Note oraz Notebook. Zaimplementuj metodę o nazwie display_notes() w klasie Notebook pozwalającą wyświetlać zawartość wszystkich notatek atrybutu instancji notes do konsoli.



Utwórz instancję klasy Notebook o nazwie notebook. Następnie wykorzystując metodę new_note() dodaj dwie notatki do notatnika o następującej treści:

'My first note.'

'My second note.'



W odpowiedzi wywołaj metodę display_notes() na instancji notebook.



Oczekiwany wynik:



My first note.
My second note."""

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
        self.notes.append(Note(content))

    def display_notes(self):
        for note in self.notes:
            print(note.content)


notebook = Notebook()
notebook.new_note('My first note.')
notebook.new_note('My second note.')
notebook.display_notes()
