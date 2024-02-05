"""Zaimplementowana jest poniższa klasa Doc przechowująca dokumenty tekstowe. Zaimplementuj metodę specjalną __lt__() pozwalającą porównywać instancje klasy Doc. Instancja klasy jest 'mniejsza' od innej instancji, gdy atrybut string zawiera mniej znaków.



Przykład:



[IN]: doc1 = Doc('Finance')
[IN]: doc2 = Doc('Education')
[IN]: print(doc1 < doc2)


[OUT]: True


Następnie utwórz dwie instancje klasy Doc dla poniższych dokumentów:

'sport'

'activity'

I przypisz odpowiednio do zmiennych:

doc1

doc2



W odpowiedzi wydrukuj wynik porównywania tych instancji, tzn. doc1 < doc2.



Oczekiwany wynik:



True"""


class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)

    def __lt__(self, other):
        return len(self.string) < len(other.string)


doc1 = Doc("sport")
doc2 = Doc("activity")
print(doc1 < doc2)
