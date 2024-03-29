"""Podana jest implementacja klasy Laptop. Zaimplementuj w klasie Laptop metodę o nazwie display_private_attrs() , która pozwoli wyświetlić nazwy atrybutów prywatnych instancji. Następnie utwórz instancję o podanych argumentach:

'Acer'

'Predator'

'AC-100'

5490

0.2



Utworzoną instancję przypisz do zmiennej laptop. W odpowiedzi wywołaj metodę display_private_attrs() na instancji laptop.



Oczekiwany wynik:



_Laptop__price
_Laptop__margin"""


class Laptop:
    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith(f"_{self.__class__.__name__}__"):
                print(attr)


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_private_attrs()
