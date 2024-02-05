"""Zaimplementuj klasę o nazwie Phone. W klasie Phone zdefiniuj dwa atrybut klasy o nazwach:

brand

model



Ustaw ich wartości odpowiednio na:

'Apple'

'iPhone X'



Następnie używając funkcji wbudowanej getattr() oraz print() wyświetl wartości podanych atrybutów klasy Phone do konsoli tak jak pokazano poniżej.



Oczekiwany wynik:



Apple
iPhone X"""


class Phone:
    brand = "Apple"
    model = "iPhone X"


print(getattr(Phone, 'brand'))

print(getattr(Phone, 'model'))
