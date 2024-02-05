"""Zaimplementowana jest poniższa klasa Hashtag przechowująca dokumenty tekstowe - hashtagi. Zaimplementuj metodę specjalną __add__() pozwalającą dodawać (sklejać) instancje klasy Hashtag za pomocą znaku spacji tak jak pokazano poniżej (weź pod uwagę odpowiednią ilość znaków '#' na początku nowego obiektu wynikowego).



Przykład:



[IN]: hashtag1 = Hashtag('sport')
[IN]: hashtag2 = Hashtag('travel')
[IN]: print(hashtag1 + hashtag2)


[OUT]: #sport #travel


Następnie utwórz trzy instancje klasy Hashtag dla poniższych dokumentów tekstowych:

'python'

'developer'

'oop'



W odpowiedzi wydrukuj wynik dodawania tych instancji do konsoli.



Oczekiwany wynik:



#python #developer #oop"""


class Hashtag:
    def __init__(self, string):
        self.string = '#' + string

    def __repr__(self):
        return f"Hashtag(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Hashtag(self.string[1:] + ' ' + other.string)


hashtag1 = Hashtag('python')
hashtag2 = Hashtag('developer')
hashtag3 = Hashtag('oop')
print(hashtag1 + hashtag2 + hashtag3)
