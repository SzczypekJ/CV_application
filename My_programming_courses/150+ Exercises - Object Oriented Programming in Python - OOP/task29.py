"""Zdefiniowane są dwie puste klasy o nazwach:

Model

View

Następnie utworzono obiekty object1, object2 oraz object3.



Wykorzystując funkcję wbudowaną isinstance() sprawdź czy obiekty object1, object2 oraz object3 są obiektami klasy Model lub klasy View. W odpowiedzi wynik wydrukuj do konsoli.



Oczekiwany wynik:



True
False
False
"""


class Model:
    pass


class View:
    pass


object1 = Model()
object2 = [Model(), Model()]
object3 = {}

print(isinstance(object1, (Model, View)))
print(isinstance(object2, (Model, View)))
print(isinstance(object3, (Model, View)))
