"""Zdefiniuj klasę o nazwie Model, która nie posiada żadnych atrybutów ani metod. Następnie utwórz instancję tej klasy o nazwie model. Wykorzystując funkcję wbudowaną isinstance() sprawdź czy obiekt model jest instancją klasy Model. Wynik wydrukuj do konsoli.



Oczekiwany wynik:



True"""


class Model:
    pass


model = Model()
print(isinstance(model, Model))
