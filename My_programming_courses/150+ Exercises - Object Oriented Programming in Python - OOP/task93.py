"""Zaimplementowana jest klasa Book. Dodaj metodę __repr__() do klasy Book będącą formalną reprezentacją instancji tej klasy (patrz wywołanie poniżej).



Następnie utwórz instancję klasy o nazwie book1 przekazując odpowiednie argumenty:

title='Inferno'

author='Dan Brown'



W odpowiedzi wydrukuj instancję book1 do konsoli.



Oczekiwany wynik:



Book(title='Inferno', author='Dan Brown')"""

import uuid


class Book:
    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book1 = Book('Inferno', 'Dan Brown')
print(book1)