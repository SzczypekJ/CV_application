"""Podana jest implementacja klasy Container:



class Container:
    This is a Container class.


Utwórz instancję klasy Container i przypisz do zmiennej container. Typ zmiennej container wydrukuj do konsoli.



Uwaga: Rozwiązanie, które przekazuje użytkownik znajduje się w pliku o nazwie exercise.py, natomiast kod sprawdzający (który jest niewidoczny dla użytkownika) wykonywany jest z pliku o nazwie evaluate.py z poziomu, którego importowana jest klasa Container. Dlatego zamiast nazwy modułu __main__ w odpowiedzi otrzymamy nazwę modułu w którym klasa ta jest zaimplementowana, czyli exercise.



Oczekiwany wynik:



<class 'exercise.Container'>"""


class Container:
    """This is a Container class."""


container = Container()

print(container.__class__)
