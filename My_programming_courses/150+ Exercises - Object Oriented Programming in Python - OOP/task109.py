"""Zaimplementowana jest poniższa klasa Doc przechowująca dokumenty tekstowe. Zaimplementuj metodę specjalną __eq__() pozwalającą porównywać instancje klasy Doc. Instancje klasy są równe, gdy posiadają identyczne wartości atrybutu string.



Przykład:



[IN]: doc1 = Doc('Finance')
[IN]: doc2 = Doc('Finance')
[IN]: print(doc1 == doc2)


[OUT]: True


Następnie utwórz dwie instancje klasy Doc dla poniższych dokumentów:

'Python'

'3.8'



W odpowiedzi wydrukuj wynik porównywania tych instancji do konsoli.



Oczekiwany wynik:



False
"""


class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)

    def __eq__(self, other):
        if self.string == other.string:
            return True
        else:
            return False
        # return self.string == other.string


doc1 = Doc("Python")
doc2 = Doc("3.8")
print(doc1 == doc2)
