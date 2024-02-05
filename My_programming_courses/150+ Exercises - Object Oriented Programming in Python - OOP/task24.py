"""Podana jest implementacja klasy Container:



class Container:
    This is a Container class.


Wyświetl wszystkie klucze atrybutu słownikowego __dict__ klasy Container do konsoli.



Oczekiwany wynik:



dict_keys(['__module__', '__doc__', '__dict__', '__weakref__'])"""


class Container:
    """This is a Container class."""


print(Container.__dict__.keys())
