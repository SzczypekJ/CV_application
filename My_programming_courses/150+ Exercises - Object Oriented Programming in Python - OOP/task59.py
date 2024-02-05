"""Zaimplementuj klasę o nazwie Laptop, która przy tworzeniu instancji ustawi poniższe atrybuty instancji:

brand jako atrybut publiczny instancji

model jako atrybut chroniony instancji

price jako atrybut prywatny instancji



Następnie utwórz instancję klasy Laptop o nazwie laptop o podanych parametrach:

'Acer'

'Predator'

5490



W odpowiedzi wydrukuj wartość atrybutu __dict__ instancji laptop do konsoli.



Oczekiwany wynik:



{'brand': 'Acer', '_model': 'Predator', '_Laptop__price': 5490}"""


class Laptop:
    def __init__(self, brand, _model, __price):
        self.brand = brand
        self._model = _model
        self.__price = __price


laptop = Laptop("Acer", "Predator", 5490)
print(laptop.__dict__)
