"""Zdefiniuj dwie klasy o nazwach Model oraz View, z których każda nie posiada żadnych atrybutów ani metod. Na podstawie tych klas utwórz dwa obiekty o nazwie model oraz view odpowiednio.



Wykorzystując funkcję wbudowaną isinstance() sprawdź czy obiekty model oraz view są instancjami klasy Model. Wynik wydrukuj do konsoli.



Oczekiwany wynik:



True
False"""


class Model:
    pass


class View:
    pass


model = Model()
view = View()
print(isinstance(model, Model))
print(isinstance(view, Model))
