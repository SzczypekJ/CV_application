"""Zdefiniowana jest klasa Book. Zaimplementuj metodę o nazwie set_title(), która pozwoli ustawić atrybut instancji o nazwie title. Przed ustawieniem wartości sprawdź czy jest to obiekt typu str, jeżeli nie zgłoś błąd TypeError o następującej treści:



'The value of the title attribute must be of str type.'


Następnie utwórz instancję klasy Book o nazwie book i wykorzystując metodę set_title() ustaw atrybut title na wartość 'Inferno'. W odpowiedzi wydrukuj wartość atrybutu title obiektu book do konsoli.



Oczekiwany wynik:



Inferno"""


class Book:
    language = 'ENG'
    is_ebook = True

    # solution 1
    # def set_title(self, title):
    #     if isinstance(title, str):
    #         self.title = title
    #     else:
    #         print('The value of the title attribute must be of str type.')

    # solution 2 probably better
    def set_title(self, value):
        if not isinstance(value, str):
            raise TypeError(
                'The value of the title attribute must be of str '
                'type.'
            )
        self.title = value


book = Book()
book.set_title("Inferno")
# print(getattr(book, 'title'))
print(book.title)
