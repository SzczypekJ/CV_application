"""Zaimplementowano klasę o nazwie Laptop, która przy tworzeniu instancji ustawia poniższe atrybuty instancji:

brand jako atrybut publiczny instancji

model jako atrybut chroniony

price jako atrybut prywatny



Następnie utworzono instancję klasy Laptop o podanych parametrach:

'Acer'

'Predator'

5490



W odpowiedzi wydrukuj wartość dla każdego atrybutu (w osobnej linii) instancji laptop tak jak pokazano poniżej.



Oczekiwany wynik:



brand -> Acer
model -> Predator
price -> 5490"""


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price


laptop = Laptop('Acer', 'Predator', 5490)

print(f'brand -> {laptop.brand}')
print(f'model -> {laptop._model}')
print(f'price -> {laptop._Laptop__price}')
