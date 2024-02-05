"""Zdefiniowane są dwie puste klasy o poniższych nazwach:

Model

View



Wykorzystując funkcję wbudowaną issubclass() sprawdź czy klasy Model oraz View są klasami pochodnymi (podklasami) klasy wbudowanej object. W odpowiedzi wynik wydrukuj do konsoli.



Oczekiwany wynik:



True
True
"""


class Model:
    pass


class View:
    pass


print(issubclass(Model, object))
print(issubclass(View, object))
