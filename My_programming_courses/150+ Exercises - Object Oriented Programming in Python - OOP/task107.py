"""Zaimplementowana jest poniższa klasa Doc przechowująca dokumenty tekstowe. Zaimplementuj metodę specjalną __add__() pozwalającą dodawać (sklejać) instancje klasy Doc za pomocą znaku spacji.



Przykład:



[IN]: doc1 = Doc('Object')
[IN]: doc2 = Doc('Oriented')
[IN]: print(doc1 + doc2)


[OUT]: Object Oriented


Następnie utwórz dwie instancje klasy Doc dla poniższych dokumentów:

'Python'

'3.8'



W odpowiedzi wydrukuj wynik dodawania tych instancji do konsoli.



Oczekiwany wynik:



Python 3.8"""


class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        string = str(self.string + " " + other.string)
        return Doc(string)
        # return Doc(self.string + ' ' + other.string)


doc1 = Doc('Python')
doc2 = Doc('3.8')
print(doc1 + doc2)
