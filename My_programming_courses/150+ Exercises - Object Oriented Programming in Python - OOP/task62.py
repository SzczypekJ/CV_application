"""Podana jest implementacja klasy Laptop. Zaimplementuj w klasie Laptop metodę o nazwie display_protected_attrs() , która pozwoli wyświetlić nazwy atrybutów chronionych instancji. Następnie utwórz instancję o podanych argumentach:

'Acer'

'Predator'

'AC-100'

5490

0.2



Utworzoną instancję przypisz do zmiennej laptop. W odpowiedzi wywołaj metodę display_protected_attrs() na instancji laptop.



Oczekiwany wynik:



_model
_code"""


class Laptop:
    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_protected_attrs(self):
        for attr in self.__dict__:
            if attr.startswith('_') and not attr.startswith(f'_{self.__class__.__name__}__'):
                print(attr) 


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_protected_attrs()
