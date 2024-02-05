"""Zaimplementowane są poniższe klasy:

Container

PlasticContainer

MetalContainer

SmallPlasticContainer



Wydrukuj do konsoli MRO - Method Resolution Order dla klasy SmallPlasticContainer.



Uwaga: Rozwiązanie, które przekazuje użytkownik znajduje się w pliku o nazwie exercise.py, natomiast kod sprawdzający (który jest niewidoczny dla użytkownika) wykonywany jest z pliku o nazwie evaluate.py z poziomu, którego importowane są klasy. Dlatego zamiast nazwy modułu __main__ w odpowiedzi otrzymamy nazwę modułu w którym klasa ta jest zaimplementowana, czyli exercise.



Oczekiwany wynik:



[<class 'exercise.SmallPlasticContainer'>, <class 'exercise.PlasticContainer'>, <class 'exercise.Container'>, <class 'object'>]"""


class Container:
    pass


class PlasticContainer(Container):
    pass


class MetalContainer(Container):
    pass


class SmallPlasticContainer(PlasticContainer):
    pass


print(SmallPlasticContainer.mro())
