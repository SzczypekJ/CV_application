"""Zdefiniowana jest klasa Book. Utworzono dwie instancje klasy Book o nazwie book_1 oraz book_2. Następnie przypisano do tych obiektów atrybuty instancji (stosując notację kropkową) odpowiednio:

do instancjibook_1:

author = 'Dan Brown'

title = 'Inferno'

do instancji book_2:

author = 'Dan Brown'

title = 'The Da Vinci Code'

year_of_publishment = 2003



Utworzono listę books składającą się z obiektów book_1 oraz book_2. Zbuduj pętlę pozwalającą wyświetlić wszystkie atrybuty instancji book_1 oraz book_2 wraz z ich wartościami tak jak pokazano poniżej (oddziel każdą instancję linią składającą się z 30 znaków '-' - myślnik tak jak pokazano poniżej).



Oczekiwany wynik:



author -> Dan Brown
title -> Inferno
------------------------------
author -> Dan Brown
title -> The Da Vinci Code
year_of_publishment -> 2003
------------------------------"""


class Book:
    language = 'ENG'
    is_ebook = True


book_1 = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

books = [book_1, book_2]

#  solution 1
for i in range(len(books)):
    for attr, value in books[i].__dict__.items():
        print(f'{attr} -> {value}')
    print('-' * 30)

# solution 2
# for attr, value in book_1.__dict__.items():
#     print(f'{attr} -> {value}')

# print('-' * 30)


# for attr, value in book_2.__dict__.items():
#     print(f'{attr} -> {value}')

# print('-' * 30)
