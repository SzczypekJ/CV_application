"""Zdefiniowana jest klasa Book. Zaimplementuj metodę o nazwie set_title(), która pozwoli ustawić atrybut instancji o nazwie title (nie dokonuj żadnej walidacji ustawianej wartości). Następnie utwórz instancję klasy Book o nazwie book i wykorzystując metodę set_title() ustaw atrybut title na wartość 'Inferno'.



W odpowiedzi wydrukuj wartość atrybutu title obiektu book do konsoli.



Oczekiwany wynik:



Inferno"""


class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, title):
        self.title = title


book = Book()
book.set_title("Inferno")
print(book.title)
# print(getattr(book, 'title')) do the same what print above
