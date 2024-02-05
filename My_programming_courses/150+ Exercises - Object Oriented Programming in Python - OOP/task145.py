"""Podane są implementacje klasy Note oraz Notebook. Zaimplementuj metodę o nazwie search() w klasie Notebook pozwalającą zwrócić listę składającą się z notatek zawierających konkretne słowo (przekazywane jako argument do metody, wielkość liter nie ma znaczenia). Możesz wykorzystać implementację metody Note.find.



Kolejno utwórz instancję klasy Notebook o nazwie notebook. Następnie wykorzystując metodę new_note() dodaj notatki do notatnika o następującej treści:

'Big Data'

'Data Science'

'Machine Learning'



W odpowiedzi wywołaj metodę search() na instancji notebook wyszukując notatek zawierających słowo 'data'.



Oczekiwany wynik:



[Note(content='Big Data'), Note(content='Data Science')]
"""
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

    def search(self, word):
        matching_notes = [note for note in self.notes if note.find(word)]
        print(matching_notes)
        # for note in matching_notes:
        #     print(note.content)


notebook = Notebook()
notebook.new_note('Big Data')
notebook.new_note('Data Science')
notebook.new_note('Machine Learning')
notebook.search("data")
