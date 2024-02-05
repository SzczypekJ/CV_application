"""Zdefiniowana jest klasa Book. Utwórz instancję klasy Book o nazwie book. Następnie wyświetl wartość atrybutu __dict__ dla instancji book. Kolejno przypisz dwa poniższe atrybuty do instancji book:

author z wartością 'Dan Brown'

title z wartością 'Inferno'



Następnie jeszcze raz wyświetl wartość atrybutu __dict__ dla instancji book do konsoli.



Oczekiwany wynik:



{}
{'author': 'Dan Brown', 'title': 'Inferno'}"""


class Book:
    language = 'ENG'
    is_ebook = True


book = Book()
print(book.__dict__)

book.author = "Dan Brown"
book.title = "Inferno"

print(book.__dict__)
