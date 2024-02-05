"""Utwórz klasę o nazwie StringListOnly rozszerzającą wbudowaną klasę list. Zmodyfikuj działanie metody append() w taki sposób, aby do listy mogły być dodawane tylko obiekty typu str. W przypadku próby dodania obiektu innego typu podnieś błąd TypeError o następującej treści:

Only objects of type str can be added to the list.



Następnie utwórz instancję klasy StringListOnly i dodaj metodą append() poniższe elementy:

'Data'

'Science'



W odpowiedzi wydrukuj utworzoną listę do konsoli.



Oczekiwany wynik:



['Data', 'Science']"""


class StringListOnly(list):
    def append(self, value):
        if isinstance(value, str):
            super().append(value)
        else:
            raise TypeError(
                "Only objects of type str can be added to the list.")


obj = StringListOnly()
obj.append("Data")
obj.append("Science")
print(obj)
