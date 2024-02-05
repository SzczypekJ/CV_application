"""Utwórz klasę o nazwie StringListOnly rozszerzającą wbudowaną klasę list. Zmodyfikuj działanie metody append() w taki sposób, aby do listy mogły być dodawane tylko obiekty typu str. Przed dodaniem obiektu do listy zamień wszystkie duże litery na małe. W przypadku próby dodania obiektu innego typu podnieś błąd TypeError o następującej treści:

Only objects of type str can be added to the list.



Następnie utwórz instancję klasy StringListOnly i dodaj metodą append() poniższe elementy:

'Data'

'Science'

'Machine Learning'



W odpowiedzi wydrukuj utworzoną listę do konsoli.



Oczekiwany wynik:



['data', 'science', 'machine learning']
"""


class StringListOnly(list):
    def append(self, value):
        if isinstance(value, str):
            super().append(value.lower())
        else:
            raise TypeError(
                "Only objects of type str can be added to the list.")


obj = StringListOnly()
obj.append("Data")
obj.append("Science")
obj.append("Machine Learning")
print(obj)
