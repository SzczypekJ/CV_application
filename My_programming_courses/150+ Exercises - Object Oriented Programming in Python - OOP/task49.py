"""Zdefiniowana jest klasa Book. Zaimplementowano metodę o nazwie set_title(), która pozwala ustawić atrybut instancji o nazwie title. Utwórz instancję klasy Book o nazwie book. Następnie korzystając z klauzuli try... except... spróbuj wykorzystując metodę set_title() ustawić wartość atrybutu title na False. W przypadku błędu TypeError wydrukuj komunikat błędu do konsoli.



Oczekiwany wynik:



The value of the title attribute must be of str type."""

class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, value):
        if not isinstance(value, str):
            raise TypeError(
                'The value of the title attribute must be of str '
                'type.'
            )
        self.title = value


book = Book()
try:
    book.set_title(False)
except TypeError as e:
    print(e)