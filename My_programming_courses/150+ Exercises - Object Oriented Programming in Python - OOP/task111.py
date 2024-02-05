"""Zaimplementowana jest poniższa klasa Doc przechowująca dokumenty tekstowe. Zaimplementuj metodę specjalną __iadd__() pozwalającą wykonywać rozszerzone przypisanie. Dwie instancje sklej za pomocą ciągu znaków ' & '.



Przykład:



[IN]: doc1 = Doc('Finance')
[IN]: doc2 = Doc('Accounting')
[IN]: doc1 += doc2
[IN]: print(doc1)


[OUT]: Finance & Accounting


Następnie utwórz dwie instancje klasy Doc dla poniższych dokumentów:

'sport'

'activity'

i przypisz odpowiednio do zmiennych:

doc1

doc2



Dokonaj rozszerzonego przypisania doc1 += doc2. W odpowiedzi wydrukuj instancję doc1 do konsoli.



Oczekiwany wynik:



sport & activity"""


class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __iadd__(self, other):
        return Doc(self.string + " & " + other.string)


doc1 = Doc("sport")
doc2 = Doc("activity")
doc1 += doc2
print(doc1)
