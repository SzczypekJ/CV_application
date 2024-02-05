"""Zdefiniowana jest klasa Book. Utwórz dwie instancje klasy Book o nazwie book_1 oraz book_2. Następnie przypisz do tych obiektów atrybuty instancji (stosując notację kropkową) odpowiednio:

do instancjibook_1:

author = 'Dan Brown'

title = 'Inferno'

do instancji book_2:

author = 'Dan Brown'

title = 'The Da Vinci Code'

year_of_publishment = 2003



W odpowiedzi wydrukuj wartość atrybutu __dict__ instancji book_1 oraz book_2.



Oczekiwany wynik:



{'author': 'Dan Brown', 'title': 'Inferno'}
{'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003}"""

class Book:
    language = 'ENG'
    is_ebook = True

book_1  = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

print(book_1.__dict__)
print(book_2.__dict__)