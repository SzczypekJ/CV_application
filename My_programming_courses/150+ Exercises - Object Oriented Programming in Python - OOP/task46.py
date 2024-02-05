"""Zdefiniowana jest klasa Book. Podana jest także lista słowników books_data zawierająca dane dotyczące dwóch książek.



books_data = [
    {
        'author': 'Dan Brown', 
        'title': 'Inferno'
    },
    {
        'author': 'Dan Brown',
        'title': 'The Da Vinci Code',
        'year_of_publishment': 2003,
    },
]


Na podstawie tych danych zbuduj dwie instancje klasy Book, gdzie atrybutami instancji będą klucze z podanych słowników wraz z ich odpowiadającymi wartościami. W odpowiedzi wydrukuj atrybuty __dict__ tak utworzonych obiektów do konsoli.



Oczekiwany wynik:



{'author': 'Dan Brown', 'title': 'Inferno'}
{'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003}"""


class Book:
    language = 'ENG'
    is_ebook = True


books_data = [
    {
        'author': 'Dan Brown',
        'title': 'Inferno'
    },
    {
        'author': 'Dan Brown',
        'title': 'The Da Vinci Code',
        'year_of_publishment': 2003,
    },
]

books = []
for i in books_data:
    book = Book()
    for attr, value in i.items():
        setattr(book, attr, value)
    books.append(book)

for i in books:
    print(i.__dict__)
