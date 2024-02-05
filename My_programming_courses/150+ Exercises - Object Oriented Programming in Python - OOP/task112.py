"""Podana jest klasa Book. Zaimplementuj metodę __str__(), która pozwoli wyświetlić nieformalną reprezentację obiektu klasy Book.



Przykład:



[IN]: book1 = Book('Inferno', 'Dan Brown')
[IN]: print(book1)


[OUT]: Book ID: 214522 | Title: Inferno | Author: Dan Brown


Następnie utwórz instancję o nazwie book przekazując argumenty:

title='The Lord of the Rings'

author='J.R.R. Tolkien'



W odpowiedzi wydrukuj instancję do konsoli.



Oczekiwany wynik:



Book ID: 183009 | Title: The Lord of the Rings | Author: J.R.R. Tolkien


Uwaga: Wartość Book ID może się różnić."""

import uuid


class Book:
    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

    def __str__(self):
        return ("Book ID: " + self.book_id + " | Title: " + self.title + " | Author: " + self.author)


book = Book(title='The Lord of the Rings', author='J.R.R. Tolkien')
print(book)
